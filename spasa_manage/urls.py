from django.urls import path
from . import spasa_manage # views.py import

urlpatterns=[
    # execute members() function in view.py when url pattern is  %root%/members/
    # project folder will be moduled named folder name
    # 
    path('home/', spasa_manage.get_user_manage_configuration, name='spasa_manage'),
]