from datetime import datetime

from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from sotongapp.models import Organ, Information
from sotongapp.serializer import InfoSerializer
# from sotongapp.decorator import organ_permission_check
from sotongapp.encrypt import get_encryptor, RSA_dec


from pathlib import Path
import os, environ


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))


@csrf_exempt
def SaveTempData(request):
    if request.method == 'POST':
        # if RSA_dec(request.COOKIES.get("Cookie", "")) != env('PEM_SECRET'):
        #     return HttpResponseForbidden
        organ = get_object_or_404(Organ, urlname=request.POST['name'])
        temp_list = request.POST.getlist('temp')
        day_list = request.POST.getlist('day')
        time_list = request.POST.getlist('time')
        for i in range(len(temp_list)):
            print("get data")
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


def AllUserCount(request):
    cnt = Information.objects.count()
    data = {
        'count': cnt
    }
    return JsonResponse(data)


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.order_by('-day', '-time')
    serializer_class = InfoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(organ__urlname=self.request.GET['search'])


def GetOrganName(request, urlname):
    organ = get_object_or_404(Organ, urlname=urlname)
    data = {
        "name": organ.name
    }
    return JsonResponse(data)