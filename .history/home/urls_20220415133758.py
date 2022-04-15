from django.urls import path
from .import views  # import our views in this folder too

urlpatterns = [

    #call the url home
    #point at the views.py file in our home folder
    path('', views.home, name='home'),
    path('bitcoinGraphs/', views.bitcoin, name='bitcoinGraphs'),
    path('cardanoGraphs/', views.cardano, name='cardanoGraphs'),
    path('dogeGraphs/', views.doge, name='dogeGraphs'),
    path('ethereumGraphs/', views.ethereum, name='ethereumGraphs'),
    path('heliumGraphs/', views.helium, name='heliumGraphs'),
    path('litecoinGraphs/', views.litecoin, name='litecoinGraphs'),
    path('polkadotGraphs/', views.polkadot, name='polkadotGraphs'),
    path('shibainuGraphs/', views.shibainu, name='shibainuGraphs'),
    path('tetherGraphs/', views.tether, name='tetherGraphs'),
]

#connect everything to our master url.py (aka cap urls.py)
