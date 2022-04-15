from django.urls import path
from .import views  # import our views in this folder too

urlpatterns = [

    #call the url home
    #point at the views.py file in our home folder
    path('', views.home, name='home'),
    path('bitcoin/', views.bitcoin, name='bitcoin'),
    path('cardano/', views.cardano, name='cardano'),
    path('doge/', views.doge, name='doge'),
    path('ethereum/', views.ethereum, name='ethereum'),
    path('helium/', views.helium, name='helium'),
    path('litecoin/', views.litecoin, name='litecoin'),
    path('polkadot/', views.polkadot, name='polkadot'),
    path('shibainu/', views.shibainu, name='shibainu'),
    path('tether/', views.tether, name='tether'),
]

#connect everything to our master url.py (aka cap urls.py)
