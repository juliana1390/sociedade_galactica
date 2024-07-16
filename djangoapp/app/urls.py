from django.urls import path
from app.views import *


app_name = 'app'

urlpatterns = [
    # app:index
    path('', index, name='index'),
    path('login_page/', login, name='login'),

    path('login_check/', login_check, name='login_check'),
    path('error_page/', login_check, name='error_page'),
    path('success_page/', login_check, name='success_page'),
    path('logout/', logout, name='logout'),
]
