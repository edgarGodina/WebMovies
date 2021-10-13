from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.core.paginator import Paginator
app_name = 'myApp'

urlpatterns = [
    path('',views.indexView,name=""),
    path('index/',views.indexView,name='index'),
    path('login/',views.loginView,name='login'),

]
