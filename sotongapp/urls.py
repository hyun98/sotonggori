
#from sotongapp.views import *

from django.urls import path, include
#from .views import infoAPI
from . import views
from rest_framework import routers

app_name = 'sotongapp'

router = routers.DefaultRouter()
router.register(r'info', views.InfoViewSet)
#router.register(r'organ', views.OrganViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path("", infoAPI),
    #path('', views.InfoList.as_view())
]