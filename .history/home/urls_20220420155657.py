from django.urls import path
from .import views  # import our views in this folder too
from django.views.generic.base import RedirectView


urlpatterns = [
    #call the url home
    #point at the views.py file in our home folder
    path('', views.home, name='home'),
    

    #Graphs
    path('bitcoinGraphs/', views.bitcoinGraphs, name='bitcoinGraphs'),
    path('cardanoGraphs/', views.cardanoGraphs, name='cardanoGraphs'),
    path('dogeGraphs/', views.dogeGraphs, name='dogeGraphs'),
    path('ethereumGraphs/', views.ethereumGraphs, name='ethereumGraphs'),
    path('heliumGraphs/', views.heliumGraphs, name='heliumGraphs'),
    path('litecoinGraphs/', views.litecoinGraphs, name='litecoinGraphs'),
    path('polkadotGraphs/', views.polkadotGraphs, name='polkadotGraphs'),
    path('shibainuGraphs/', views.shibainuGraphs, name='shibainuGraphs'),
    path('tetherGraphs/', views.tetherGraphs, name='tetherGraphs'),

    #Histories
    path('bitcoinHistory/', views.bitcoinHistory, name='bitcoinHistory'),
    path('cardanoHistory/', views.cardanoHistory, name='cardanoHistory'),
    path('dogeHistory/', views.dogeHistory, name='dogeHistory'),
    path('ethereumHistory/', views.ethereumHistory, name='ethereumHistory'),
    path('heliumHistory/', views.heliumHistory, name='heliumHistory'),
    path('litecoinHistory/', views.litecoinHistory, name='litecoinHistory'),
    path('polkadotHistory/', views.polkadotHistory, name='polkadotHistory'),
    path('shibainuHistory/', views.shibainuHistory, name='shibainuHistory'),
    path('tetherHistory/', views.tetherHistory, name='tetherHistory'),




    path('bitcoinGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('bitcoinGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('bitcoinGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('bitcoinGraphs/ethereumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    # path('bitcoin/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('bitcoin/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('bitcoin/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('bitcoin/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('bitcoin/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('bitcoin/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('cardano/bitcoin/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('cardano/cardano/', RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('cardano/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('cardano/ethereum/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('cardano/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('cardano/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('cardano/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('cardano/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('cardano/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('cardano/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('doge/bitcoin/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('doge/cardano/', RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('doge/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('doge/ethereum/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('doge/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('doge/litecoin/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('doge/polkadot/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('doge/shibainu/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('doge/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('doge/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('ethereum/bitcoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('ethereum/cardano/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('ethereum/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('ethereum/ethereum/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('ethereum/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('ethereum/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('ethereum/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('ethereum/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('ethereum/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('ethereum/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('helium/bitcoin/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('helium/cardano/', RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('helium/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('helium/ethereum/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('helium/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('helium/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('helium/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('helium/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('helium/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('helium/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('litecoin/bitcoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('litecoin/cardano/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('litecoin/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('litecoin/ethereum/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('litecoin/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('litecoin/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('litecoin/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('litecoin/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('litecoin/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('litecoin/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('polkadot/bitcoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('polkadot/cardano/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('polkadot/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('polkadot/ethereum/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('polkadot/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('polkadot/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('polkadot/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('polkadot/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('polkadot/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('polkadot/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('shibainu/bitcoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('shibainu/cardano/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('shibainu/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('shibainu/ethereum/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('shibainu/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('shibainu/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('shibainu/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('shibainu/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('shibainu/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('shibainu/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    # path('tether/bitcoin/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoin/')),
    # path('tether/cardano/', RedirectView.as_view(url='http://127.0.0.1:8000/cardano/')),
    # path('tether/doge/', RedirectView.as_view(url='http://127.0.0.1:8000/doge/')),
    # path('tether/ethereum/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/ethereum/')),
    # path('tether/helium/', RedirectView.as_view(url='http://127.0.0.1:8000/helium/')),
    # path('tether/litecoin/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/litecoin/')),
    # path('tether/polkadot/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/polkadot/')),
    # path('tether/shibainu/',
    #      RedirectView.as_view(url='http://127.0.0.1:8000/shibainu/')),
    # path('tether/tether/', RedirectView.as_view(url='http://127.0.0.1:8000/tether/')),
    # path('tether/home/', RedirectView.as_view(url='http://127.0.0.1:8000/'))







]

#connect everything to our master url.py (aka cap urls.py)
