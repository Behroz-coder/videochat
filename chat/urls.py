from django.urls import path
from .views import peer1, peer2, peer

urlpatterns = [
    path('', peer, name='peer'),
    path('peer1/', peer, name='peer'),
    path('peer2/', peer, name='peer'),
]