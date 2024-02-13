from django.urls import path
from core1.views import engine, packages


urlpatterns = [
    path('p/engine',engine, name="reg"),
    path('p/packages',packages, name="packages"),
]
