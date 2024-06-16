from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('/getquerry',views.getquerry,name='getquerry'),
    path('/sortdata',views.sortdata,name='sortdata')
]