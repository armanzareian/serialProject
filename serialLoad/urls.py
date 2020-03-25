from django.urls import path,include
from serialLoad.views import loadserial
urlpatterns = [
     path('',loadserial)
]
