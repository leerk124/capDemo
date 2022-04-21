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



    #BITCOIN GRAPH TO GRAPH
    path('bitcoinGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('bitcoinGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('bitcoinGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('bitcoinGraphs/ethereumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('bitcoinGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('bitcoinGraphs/litecoins/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('bitcoinGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('bitcoinGraphs/shibainuGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('bitcoinGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('bitcoinGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),

    #BITCOIN GRAPH TO HISTORY
    path('bitcoinGraphs/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('bitcoinGraphs/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('bitcoinGraphs/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('bitcoinGraphs/ethereumHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('bitcoinGraphs/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('bitcoinGraphs/litecoinHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('bitcoinGraphs/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('bitcoinGraphs/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('bitcoinGraphs/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),
    path('bitcoinGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),


    #BITCOIN HISTORY TO HISTORY
    path('bitcoinHistory/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('bitcoinHistory/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('bitcoinHistory/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('bitcoinGraphs/ethereumHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('bitcoinGraphs/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('bitcoinGraphs/litecoinHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('bitcoinGraphs/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('bitcoinGraphs/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('bitcoinGraphs/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),
    path('bitcoinGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),





    #CARDANO
    path('cardanoGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('cardanoGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('cardanoGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('cardanoGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('cardanoGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('cardanoGraphs/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('cardanoGraphs/polkotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('cardanoGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    path('cardanoGraphs/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('cardanoGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),


    #DOGE
    path('dogeGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('dogeGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('dogeGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('dogeGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('dogeGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('dogeGraphs/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('dogeGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('dogeGraphs/shibainuGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('dogeGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('dogeGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),

    #ETHEREUM
    path('ethereumGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('ethereumGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('ethereumGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('ethereumGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('ethereumGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('ethereumGraphs/litecoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('ethereumGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('ethereumGraphs/shibainuGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('ethereumGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('ethereumGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    
    #HELIUM
    path('heliumGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('heliumGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('heliumGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('heliumGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('heliumGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('heliumGraphs/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('heliumGraphs/polkadotGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('heliumGraphs/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('heliumGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('heliumGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    
    #LITECOIN
    path('litecoinGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('litecoinGraphs/cardanoGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('litecoinGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('litecoinGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('litecoinGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('litecoinGraphs/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('litecoinGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('litecoinGraphs/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('litecoinGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('litecoinGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    
    #POLAKDOT
    path('polkadotGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('polkadotGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('polkadotGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('polkadotGraphs/ethereumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('polkadotGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('polkadotGraphs/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('polkadotGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('polkadotGraphs/shibainuGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('polkadotGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('polkadotGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),


    #SHIBAINU
    path('shibainuGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('shibainuGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('shibainuGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('shibainuGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('shibainuGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('shibainuGraphs/litecoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('shibainuGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('shibainuGraphs/shibainuGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('shibainuGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('shibainuGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),

    #TETHER
    path('tetherGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('tetherGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('tetherGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('tetherGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('tetherGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('tetherGraphs/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('tetherGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('tetherGraphs/shibainuGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('tetherGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('tetherGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/'))



]

#connect everything to our master url.py (aka cap urls.py)
