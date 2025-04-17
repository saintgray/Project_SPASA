from django.shortcuts import render
from django.http import HttpResponse

class Handler:
    
    def __init__(self):
        super()
        
    def response(self, request):
        print('handler 010 received')
        return HttpResponse(render(template_name='view_account_010', request=request))
