from django.contrib import admin
# import django.apps

# Register your models here.
from .models import Product

# models = django.apps.apps.get_models()
# print(models)

admin.site.register(Product)