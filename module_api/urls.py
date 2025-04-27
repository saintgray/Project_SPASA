from django.urls import path
import module_api.auth.authorize_service as authorize_service

urlpatterns=[
    # execute members() function in view.py when url pattern is  %root%/members/
    # project folder will be moduled named folder name
    # 
    path('sign-in/', authorize_service.process_sign_in),
    path('sign-up/', authorize_service.process_sign_up),
    path('sign-out/', authorize_service.process_sign_out),
    
    
]