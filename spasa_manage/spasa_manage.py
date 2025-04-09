from django.shortcuts import render
from django.http import HttpResponse
from authentication import ACCESSIBLE_VIEW

# get overview datas for 
def get_view_permission(request):
    # return HttpResponse("Hello world")    
    # if you want to render with template, you have to declare this modules in INSTALLED_APPS at %ROOT%/PROJECT/settings.py
    # loader.get_template('manage_overview.html').render()
    context={
        'views':request.session.__getitem__(ACCESSIBLE_VIEW)
    }
    return HttpResponse(render(template_name='manage_overview.html', request=request, context=context))