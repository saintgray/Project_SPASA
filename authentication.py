from module_api.auth import authorize_service as AUTH
import json

def pre_handle_request(get_response):
    def authorized_user(request):
        # cookie=request.COOKIES
        session=request.session
        provided_menu_to_user=session.__contains__(AUTH.ACCESSIBLE_VIEW_KEY)
        has_been_authorized=session.__contains__(AUTH.UESR_KEY)
        if provided_menu_to_user:
            print('trace accessible view')
            print(session.__getitem__(AUTH.ACCESSIBLE_VIEW_KEY), end='\n======================\n')
        else:
            if not has_been_authorized:
                print('assign user info')
                # TODO get user info contains user auth level
                # psuedo code
                # user <-- user info contains user id, auth level etc..
                session.__setitem__(AUTH.UESR_KEY, {'auth_level': AUTH.PUBLIC_AUTH_LEVEL}) # example
            # TODO raise exception if user dosen't have authorized on requested resources (=view)
            # psuedo code
            # view <-- requested view id
            # if not contains (e, l) # list(l) of accessible view info(e)
            # raise exception
            session.__setitem__(AUTH.ACCESSIBLE_VIEW_KEY, json.loads(json.dumps(AUTH.get_view_permissions(request))))
        return get_response(request)
    return authorized_user
    
        
        