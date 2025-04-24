from django.http import HttpResponse
from django.http import JsonResponse
from django.http.response import HttpResponseBase
from django.http import HttpRequest
from rest_framework import serializers
from rest_framework.decorators import api_view
from dataclasses import dataclass
from module_api.decorator.request import post_request
from module_entity.model_view import View
from module_entity.model_view import ViewModel
from module_entity.model_member import MemberModel
from module_entity.model_member import Member
from datetime import datetime
from datetime import date
import traceback
import json 
from typing import Final


UESR_KEY: Final = 'USER'
PUBLIC_AUTH_LEVEL: Final = 3
MEMBER_USER_LEVEL: Final = 2
ACCESSIBLE_VIEW_KEY: Final='VIEW'

@api_view(['POST'])
def process_sign_in(request):
    print('progress sign in start ====================> ' + request.path_info)
    user_id=request.POST.get('id')
    user_pw=request.POST.get('password')
    try:
        user = Member(MemberModel.objects.get(id__iexact=user_id, password__exact=user_pw)).data
        request.session.__setitem__(UESR_KEY, user)
        request.session.__setitem__(ACCESSIBLE_VIEW_KEY, get_view_permissions(request))
        return JsonResponse({'status': 200})
    except MemberModel.DoesNotExist:
        return JsonResponse({'status': 404})
    except Exception:
        return JsonResponse({'status': 500})
    
@api_view(['POST'])
def process_sign_up(request):
    print('progress sign in start ====================> ' + request.path_info)
    x = request.data
    print(x)
    print(x['id'])
    print(x['password'])
    try:
        user_id=x['id']
        pw = x['password']
        user = get_user(user_id)
        if user is not None:
            return JsonResponse({'status': 400})
            
        mm = Member(data={
                'id':user_id
                ,'password':pw
                ,'auth_level':'2'
                ,'create_by':'APP'
                ,'create_date':datetime.now()
                ,'update_by':'APP'
                ,'update_date':datetime.now()
        }) 
        print(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        print(mm.is_valid(raise_exception=True))
        mm.save()
        return JsonResponse({'status': 200})
    except Exception as e:
        print('excpetion occured')
        print(traceback.format_exc())
        return JsonResponse({'status': 500})

def get_view_permissions(request):
    user_auth_level=request.session.__getitem__(UESR_KEY).get('auth_level')
    return View(ViewModel.objects.filter(auth_level__gte=user_auth_level).order_by('view_id'), many=True).data

def get_user(user_id):
    try:
        user = Member(MemberModel.objects.get(id__iexact=user_id))
    except MemberModel.DoesNotExist:
        user = None
    finally:
        return user
    
    
    