from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from sotongapp.views import *

app_name = 'sotongapp'

router = routers.DefaultRouter()
router.register(r'info', InfoViewSet)
router.register(r'organs', OrganViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('save/', SaveTempData),
]