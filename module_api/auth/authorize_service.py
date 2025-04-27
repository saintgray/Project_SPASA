from django.conf import settings
from django.http import JsonResponse
from django.db import transaction
from rest_framework.decorators import api_view
from module_entity.model_view import View
from module_entity.model_view import ViewModel
from module_entity.model_member import MemberModel
from module_entity.model_member import Member
import traceback
import json 
from module_api.enum import UESR_KEY, ACCESSIBLE_VIEW_KEY, MEMBER_USER_LEVEL

@api_view(['POST'])
def process_sign_in(request):
    print(settings)
    print(settings.SESSION_ENGINE)
    print('progress sign in start ====================> ' + request.path_info)
    body = json.loads(request.data['user'])
    try: 
        user = Member(MemberModel.objects.get(id__iexact=body['id'], password__exact=body['password'])).data
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
    try:
        body = json.loads(request.POST.get('user'))
        user = get_user(body['id'])
        
        if user is not None:
            Member(data = user).save(request)
            return JsonResponse({'status': 400}) # Duplicated User
        with transaction.atomic():
            body.__setitem__('auth_level', MEMBER_USER_LEVEL)
            user = Member(data=body).save(request)
            request.session.__setitem__(UESR_KEY, Member(user).data)
            request.session.__setitem__(ACCESSIBLE_VIEW_KEY, get_view_permissions(request))
            return JsonResponse({'status': 200})
    except Exception as e:
        print(traceback.format_exc())
        return JsonResponse({'status': 500})

@api_view(['POST'])
def process_sign_out(request):
    print(request)
    return JsonResponse({'status': 200})

def get_view_permissions(request):
    user_auth_level=request.session.__getitem__(UESR_KEY).get('auth_level')
    return View(ViewModel.objects.filter(auth_level__gte=user_auth_level).order_by('view_id'), many=True).data

def get_user(user_id):
    try:
        user = Member(MemberModel.objects.get(id__iexact=user_id)).data
    except MemberModel.DoesNotExist:
        user = None
    finally:
        return user
    
    
    