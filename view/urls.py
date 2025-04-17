from django.urls import path
from . import abstract_handler
# urlpatterns=[
#     path('login/', spasa_manage.get_view_permission, name='spasa_manage'),
# ]
urlpatterns = [
    path('login/', abstract_handler.handle),
    path('main/', abstract_handler.handle),
    path('test/', abstract_handler.handle)
]
    