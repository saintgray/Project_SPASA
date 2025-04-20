from django.shortcuts import render
from django.http import HttpResponse
from .view_account_010.handler import Handler as Account_Handler_010
from .view_main_010.handler import Handler as Main_Handler_010
from .view_faq_010.handler import Handler as Faq_Handler_010

CONFIG={
    '/view/login/':Account_Handler_010(),
    '/view/main/':Main_Handler_010(),
    '/view/faq/':Faq_Handler_010()
}

class AbstractHandler:
    
    def __init__(self):
        super()
        
    @staticmethod
    def response(request):
        print(dir(CONFIG))
        path=request.path_info
        views=request.session.__getitem__('VIEW')
        has_permission=False
        print('===== path : ' + str(path))
        for view in views:
            print(view)
            has_permission = (path == view['route_url'])
            if has_permission:
                break
        if not has_permission or not CONFIG.__contains__(path):
            return HttpResponse(render(template_name='not_found', request=request))    
        else:
            return CONFIG[path].response(request=request)
            
def handle(request):
    # path=list(filter(lambda e: e !='', request.path_info.split('/')))
    return AbstractHandler.response(request)
    
    

    
    
    
    