from datetime import date, datetime
from django.conf.urls import url
from django.core.checks.messages import Info

from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from sotongapp.models import Organ, Information
from sotongapp.serializer import InfoSerializer, OrganSerializer
from sotongapp.encrypt import get_encryptor, RSA_dec
from sotongapp.utils import get_maxvnum_avgnum
# from sotongapp.decorator import organ_permission_check

from pathlib import Path
import os, environ


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))


class PublicApiMixin:
    authentication_classes = ()
    permission_classes = ()


@csrf_exempt
def SaveTempData(request):
    if request.method == 'POST':
        organ = get_object_or_404(Organ, urlname=request.POST['name'])
        temp_list = request.POST.getlist('temp')
        day_list = request.POST.getlist('day')
        time_list = request.POST.getlist('time')
        for i in range(len(temp_list)):
            day = datetime.strptime(day_list[i], "%Y-%m-%d")
            time = datetime.strptime(time_list[i], "%H:%M:%S")
            temp = round(float(temp_list[i]), 2)
            info = Information(organ=organ, temp=temp, \
                                day=day, time=time)
            info.save()
        
        return HttpResponse("got it")
    else:
        response = HttpResponse("send token")
        response.set_cookie('RSA-token', get_encryptor())
        return response

class SaveTempDataApi(PublicApiMixin, APIView):
    def post(self, request, *args, **kwargs):
        organ = get_object_or_404(Organ, urlname=request.data.get('organ', ''))
        day = request.data.get('date', '')
        time = request.data.get('time', '')
        temp = request.data.get('temp', '')
        
        day = datetime.strptime(day, "%Y-%m-%d")
        time = datetime.strptime(time, "%H:%M:%S")
        temp = round(float(temp), 2)
        info = Information(organ=organ, temp=temp, day=day, time=time)
        info.save()
        
        return Response({
            "message": "Success get data",
        }, status=status.HTTP_200_OK)
        

def AllUserCount(request):
    cnt = Information.objects.count()
    data = {
        'count': cnt
    }
    return JsonResponse(data)


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.order_by('-day', '-time')
    serializer_class = InfoSerializer
    
    permission_classes = []
    authentication_classes = []
    
    def get_queryset(self):
        return super().get_queryset().filter(organ__urlname=self.request.GET['search'])


def GetOrganName(request, urlname):
    organ = get_object_or_404(Organ, urlname=urlname)
    data = {
        "name": organ.name
    }
    return JsonResponse(data)


class GetVisitorView(APIView):
    
    def get(self, request, urlname):
        organ = get_object_or_404(Organ, urlname=urlname)
        totaluser = Information.objects.filter(organ=organ).count()
        todayuser = Information.objects.filter(
            Q(day=datetime.today()) &\
            Q(organ=organ)
        ).count()
        avguser, maxuser = get_maxvnum_avgnum(totaluser, organ)
        
        data = {
            "totaluser": totaluser,
            "todayuser": todayuser,
            "avguser": avguser,
            "maxuser": maxuser
        }
        
        return Response(data)
    