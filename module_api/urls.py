from django.urls import path
from module_api.auth.authorize_service import process_sign_in
from module_api.auth.authorize_service import process_sign_up

urlpatterns=[
    # execute members() function in view.py when url pattern is  %root%/members/
    # project folder will be moduled named folder name
    # 
    path('sign-in/', process_sign_in),
    path('sign-up/', process_sign_up),
    
    
]