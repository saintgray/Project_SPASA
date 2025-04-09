from spasa_model.entry.model_view import ViewModel
from spasa_model.entry.model_view import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

def pre_handle_request(get_response):    
    PUBLIC_AUTH_LEVEL=3
    def authorized_user(request):
        # cookie=request.COOKIES
        session=request.session
        if session.__contains__('PERMISSIONS'):
            print('user permissions --->')
            print(session.__getitem__('PERMISSIONS'), end='\n======================\n')
        else:
            print('set permissions on session')
            auth_level = PUBLIC_AUTH_LEVEL if not session.__contains__('USER_ID') else session.__getitem__('USER_ID').auth_level
            permissions=View(ViewModel.objects.filter(auth_level__gte=auth_level).order_by('view_id'), many=True).data
            print(permissions)
            print(json.loads(json.dumps(permissions)))
            session.__setitem__('PERMISSIONS', json.loads(json.dumps(permissions)))
            print(type(json.loads(json.dumps(permissions)))) # generic
            # print(type(JSONParser(io.BytesIO(JSONRenderer.render(permissions))))) # dict
        return get_response(request)
    return authorized_user
    
        
        