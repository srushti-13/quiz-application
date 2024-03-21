from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('',home,name='home'),
    path('view_score' , View_score , name="view_score"),
    path('api/check_score', check_score,name='check_score'),
    path('<id>',take_quiz,name='take_quiz'),
    path('api/<id>',api_question,name='api_question')
    

    
]
