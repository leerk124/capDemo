from django.urls import path
from .import views  # import our views in this folder too

urlpatterns = [
    #call the url home
    #point at the views.py file in our home folder
    path('', views.home, name='home'),
    path('bitcoinGraphs/', views.bitcoinGraphs, name='bitcoinGraphs'),
    path('cardanoGraphs/', views.cardanoGraphs, name='cardanoGraphs'),
    path('dogeGraphs/', views.dogeGraphs, name='dogeGraphs'),
    path('ethereumGraphs/', views.ethereumGraphs, name='ethereumGraphs'),
    path('heliumGraphs/', views.heliumGraphs, name='heliumGraphs'),
    path('litecoinGraphs/', views.litecoinGraphs, name='litecoinGraphs'),
    path('polkadotGraphs/', views.polkadotGraphs, name='polkadotGraphs'),
    path('shibainuGraphs/', views.shibainuGraphs, name='shibainuGraphs'),
    path('tetherGraphs/', views.tetherGraphs, name='tetherGraphs'),

    path('bitcoinHistory/', views.bitcoinHistory, name='bitcoinHistory'),
    path('cardanoHistory/', views.cardanoHistory, name='cardanoHistory'),
    path('dogeHistory/', views.dogeHistory, name='dogeHistory'),
    path('ethereumHistory/', views.ethereumHistory, name='ethereumHistory'),
    path('heliumHistory/', views.heliumHistory, name='heliumHistory'),
    path('litecoinHistory/', views.litecoinHistory, name='litecoinHistory'),
    path('polkadotHistory/', views.polkadotHistory, name='polkadotHistory'),
    path('shibainuHistory/', views.shibainuHistory, name='shibainuHistory'),
    path('tetherHistory/', views.tetherHistory, name='tetherHistory'),


]

#connect everything to our master url.py (aka cap urls.py)
