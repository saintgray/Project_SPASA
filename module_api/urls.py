from django.urls import path
from module_api.auth.authorize_service import get_view_permissions

urlpatterns=[
    # execute members() function in view.py when url pattern is  %root%/members/
    # project folder will be moduled named folder name
    # 
    path('permission/', get_view_permissions, name='spasa_manage'),
]