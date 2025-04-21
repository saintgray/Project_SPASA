from django.http import HttpResponse
from django.http import JsonResponse
from django.http.response import HttpResponseBase
from rest_framework.decorators import api_view
from module_entity.model_view import View
from module_entity.model_view import ViewModel
from module_entity.model_member import MemberModel
from module_entity.model_member import Member
import json 


UESR_KEY='USER'
PUBLIC_AUTH_LEVEL=3
ACCESSIBLE_VIEW_KEY='VIEW'



@api_view(['POST'])
def process_sign_in(request):
    print('progress sign in start ====================> ' + request.path_info)
    user_id=request.POST.get('form_id')
    user_pw=request.POST.get('form_pw')
    try:
        user = Member(MemberModel.objects.get(id__iexact=user_id, password__exact=user_pw)).data
        request.session.__setitem__(UESR_KEY, user)
        request.session.__setitem__(ACCESSIBLE_VIEW_KEY, get_view_permissions(request))
        return JsonResponse({'status': 200})
    except MemberModel.DoesNotExist:
        return JsonResponse({'status': 404})
    except:
        return JsonResponse({'status': 500})

def get_view_permissions(request):
    user_auth_level=request.session.__getitem__(UESR_KEY).get('auth_level')
    return View(ViewModel.objects.filter(auth_level__gte=user_auth_level).order_by('view_id'), many=True).data

def get_user(user_id):
    return MemberModel.objects.get(id__iexact=user_id)
    
    
    