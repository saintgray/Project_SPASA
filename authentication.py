from spasa_model.entry.model_view import ViewModel
from spasa_model.entry.model_view import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

PUBLIC_AUTH_LEVEL=3
ACCESSIBLE_VIEW='VIEW'
UESR_KEY='USER'

def pre_handle_request(get_response):    
    
    
    def authorized_user(request):
        # cookie=request.COOKIES
        session=request.session
        provided_menu_to_user=session.__contains__(ACCESSIBLE_VIEW)
        has_been_authorized=session.__contains__(UESR_KEY)
        
        if provided_menu_to_user:
            print('trace accessible view')
            print(session.__getitem__(ACCESSIBLE_VIEW), end='\n======================\n')
        else:
            if not has_been_authorized:
                print('assign user info')
                # TODO get user info contains user auth level
                # psuedo code
                # user <-- user info contains user id, auth level etc..
                session.__setitem__(UESR_KEY, {'auth_level': PUBLIC_AUTH_LEVEL}) # example
            auth_level = session.__getitem__(UESR_KEY).get('auth_level')
            accessible_views=View(ViewModel.objects.filter(auth_level__gte=auth_level).order_by('view_id'), many=True).data
            # TODO raise exception if user dosen't have authorized on requested resources (=view)
            # psuedo code
            # view <-- requested view id
            # if not contains (e, l) # list(l) of accessible view info(e)
            # raise exception
            session.__setitem__(ACCESSIBLE_VIEW, json.loads(json.dumps(accessible_views)))
        return get_response(request)
    return authorized_user
    
        
        