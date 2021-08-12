from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from sotongapp.views import *

app_name = 'sotongapp'

router = routers.DefaultRouter()
router.register(r'info', InfoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('save/', SaveTempData),
    path('usercnt/', UsedUserCount),
    path('organ/<str:urlname>', getOrgandata),
]
