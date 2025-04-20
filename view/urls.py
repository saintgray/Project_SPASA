from django.urls import path
from django.urls import path, re_path
from . import abstract_handler
# urlpatterns=[
#     path('login/', spasa_manage.get_view_permission, name='spasa_manage'),
# ]
urlpatterns = [
    re_path(r'.+/$', abstract_handler.handle),
    # path('main/', abstract_handler.handle),
    # path('test/', abstract_handler.handle)
]
    