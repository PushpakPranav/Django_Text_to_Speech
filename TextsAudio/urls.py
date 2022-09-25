from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="TextsAudio"),
    path('result',views.result,name='result'),
]