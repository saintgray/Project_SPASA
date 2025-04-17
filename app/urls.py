from django.urls import include, path

urlpatterns = [
    path('api/', include('module_api.urls')),
    path('view/', include('view.urls')),   
]
