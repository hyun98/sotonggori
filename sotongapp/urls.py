from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from sotongapp.views import SaveTempData, AllUserCount, GetOrganName,\
    GetVisitorView, InfoViewSet, SaveTempDataApi

app_name = 'sotongapp'

router = routers.DefaultRouter()
router.register(r'info', InfoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('save/', SaveTempDataApi.as_view()),
    path('usercnt/', AllUserCount),
    path('organ/<str:urlname>', GetOrganName),
    path('visitor/<str:urlname>', GetVisitorView.as_view()),
]
