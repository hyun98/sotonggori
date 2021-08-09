#from rest_framework.response import Response
#from rest_framework.decorators import api_view
from .serializers import InfoSerializer, OrganSerializer
#from rest_framework.views import APIView
from rest_framework import viewsets

# from django.http import Http404
# from rest_framework import status
# from rest_framework.response import Response
from .models import Organ, Information


#FBV방식(?)내가 젤 처음 한거
# @api_view(['GET'])
# def infoAPI(request):

#     info_list = Information.objects.order_by('-organ_name', '-day', '-time')
#     print(info_list)
#     serializer = InfoSerializer(info_list, many=True)

#     return Response(serializer.data)

# class OrganViewSet(viewsets.ModelViewSet):
#     queryset = Organ.objects.all()
#     serializer_class = OrganSerializer



#ViewSet방식
class InfoViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.order_by('-organ_name', '-day', '-time')
    #queryset = Information.objects.all()
    serializer_class = InfoSerializer

    def get_queryset(self):

        qs = super().get_queryset()

        search = self.request.query_params.get('search','')
        if search:
            qs = qs.filter(organ_name=search)

        return qs



#CBV방식 일단 따라하기
# class InfoList(APIView):

#     def post(self, request, format=None):
#         serializer = InfoSerializer(data=request.data)

#         if  serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
    

#     def get(self, request, format=None):
#         info_list = Information.objects.order_by('-organ_name', '-day', '-time')
#         serializer = InfoSerializer(info_list, many=True)
#         return Response(serializer.data)


