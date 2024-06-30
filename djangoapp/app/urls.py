from django.urls import path
from app.views import *
from . import views

app_name = 'app'

urlpatterns = [
    # app:index
    path('', index, name='index'),
    path('login_page/', login, name='login'),
    path('login_check/', login_check, name='login_check'),
]
