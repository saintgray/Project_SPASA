from django.shortcuts import render
from django.http import HttpResponse

class Handler:
    
    def __init__(self):
        super()
        
    def response(self, request):
        return HttpResponse(render(template_name='view_main_010.html', request=request))
