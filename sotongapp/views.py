from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework.response import Response
#from rest_framework.decorators import api_view
from .serializers import InfoSerializer, OrganSerializer
#from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Organ, Information
from .forms import InfoForm


#FBV방식(?)내가 젤 처음 한거
# @api_view(['GET'])
# def infoAPI(request):

#     info_list = Information.objects.order_by('-organ_name', '-day', '-time')
#     print(info_list)
#     serializer = InfoSerializer(info_list, many=True)

#     return Response(serializer.data)




#ViewSet방식
class InfoViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.order_by('-organ_name', '-day', '-time')
    serializer_class = InfoSerializer

    def get_queryset(self):

        qs = super().get_queryset()

        search = self.request.query_params.get('search','')

        if search:
            qs = qs.filter(organ_name=search)

        return qs


class OrganViewSet(viewsets.ModelViewSet):
    queryset = Organ.objects.all()
    serializer_class = OrganSerializer




def info_create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            info = form.save()
            info.save()
            return render(request, 'sotongapp/test.html')
    
    else:
        form = InfoForm()
    
    content = {'form': form }
    return render(request, 'sotongapp/info_create.html', content)
