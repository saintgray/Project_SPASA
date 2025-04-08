from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader


# get overview datas for 
def get_user_manage_configuration(request):
    # return HttpResponse("Hello world")    
    # if you want to render with template, you have to declare this modules in INSTALLED_APPS at %ROOT%/PROJECT/settings.py
    # loader.get_template('manage_overview.html').render()
    test(y=4, x=3)
    return HttpResponse(render(template_name='manage_overview.html', request=request))
    # return HttpResponse(loader.get_template('manage_overview.html').render())
    
def test(x, y):
    print(str(x)  + " : " + str(y))
    