from module_entity.model_view import View
from module_entity.model_view import ViewModel

UESR_KEY='USER'
PUBLIC_AUTH_LEVEL=3
ACCESSIBLE_VIEW_KEY='VIEW'

def get_view_permissions(request):
    user_auth_level=request.session.__getitem__(UESR_KEY).get('auth_level')
    return View(ViewModel.objects.filter(auth_level__gte=user_auth_level).order_by('view_id'), many=True).data