from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contador.views import Screen

router = routers.DefaultRouter()
router.register(r'contador', Screen, basename='contador')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]