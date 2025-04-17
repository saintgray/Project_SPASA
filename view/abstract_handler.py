from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .view_account_010.handler import Handler as Account_Handler_010
from .view_main_010.handler import Handler as Main_Handler_010

CONFIG={
    '/view/login/':Account_Handler_010(),
    '/view/main/':Main_Handler_010()
}

class AbstractHandler:
    
    def __init__(self):
        super()
        
    @staticmethod
    def response(request):
        print(dir(CONFIG))
        if not CONFIG.__contains__(request.path_info):
            return HttpResponse(render(template_name='not_found', request=request))
        else:
            return CONFIG[request.path_info].response(request=request)
            
def handle(request):
    # path=list(filter(lambda e: e !='', request.path_info.split('/')))
    return AbstractHandler.response(request)
    
    

    
    
    
    