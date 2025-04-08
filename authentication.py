from spasa_model.model_auth import Auth
# from spasa_model.model_view import View;

def pre_handle_request(get_response):
    def authorized_user(request):
        # cookie=request.COOKIES
        session=request.session
        
        if session.__contains__('PERMISSIONS'):
            print('user permissions --->')
            print(session.__getitem__('PERMISSIONS'), end='\n======================\n')
        else:
            #TODO MAP USER'S VIEW AUTHORITIES (=MENU, FUNCTIONS)
            print('set permissions on session')
            session.__setitem__('PERMISSIONS', 'MY PERMISSION JSON DATA')
            
        # View.get_deferred_fields
        # print(cookie.get('csrftoken'))
        
        # print('authorized_user process start ...')
        # auth_list=Auth.objects.filter(auth_level=1)
        # for i in range(len(auth_list)):
        #     print('auth level : ' + auth_list[i].auth_level)
        #     print('auth desc : ' + auth_list[i].auth_desc)
        # print(Auth.objects.all())
        return get_response(request)
    # call inner function
    return authorized_user
    
        