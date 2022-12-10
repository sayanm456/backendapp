from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backendapi import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/', include(router.urls)),
]
