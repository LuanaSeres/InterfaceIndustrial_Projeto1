from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contador.views import Screen

router = routers.DefaultRouter()
router.register(r'count', Screen, basename='count')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]