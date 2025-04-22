from django.shortcuts import render
from django.http import HttpResponse

class Handler:
    
    def __init__(self):
        print('init view account 010 handler', end="\n\n")
        super()
        
    def response(self, request):
        return HttpResponse(render(template_name='view_account_010.html', request=request))
