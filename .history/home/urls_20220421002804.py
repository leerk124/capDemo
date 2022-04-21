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


    ###############################BITCOIN######################################
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

    #BITCOIN HISTORY TO GRAPH
    path('bitcoinHistory/bitcoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('bitcoinHistory/cardanoGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('bitcoinHistory/dogeGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('bitcoinHistory/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('bitcoinHistory/heliumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('bitcoinHistory/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('bitcoinHistory/polkadotGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('bitcoinHistory/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('bitcoinHistory/tetherGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('bitcoinHistory/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),

    #BITCOIN HISTORY TO HISTORY
    path('bitcoinGraphs/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('bitcoinGraphs/cardanoHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('bitcoinGraphs/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('bitcoinGraphs/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('bitcoinGraphs/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('bitcoinGraphs/litecoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('bitcoinGraphs/polkadotHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('bitcoinGraphs/shibainuHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('bitcoinGraphs/tetherHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),


    #############################################CARDANO##############################
    #CARDANO GRAPH TO GRAPH
    path('cardanoGraphs/bitcoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('cardanoGraphs/cardanoGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('cardanoGraphs/dogeGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('cardanoGraphs/ethereumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('cardanoGraphs/heliumGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('cardanoGraphs/litecoinGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('cardanoGraphs/polkadotGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('cardanoGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    path('cardanoGraphs/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('cardanoGraphs/tetherGraphs/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),

    #CARDANO GRAPH TO HISTORY
    path('cardanoGraphs/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('cardanoGraphs/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('cardanoGraphs/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('cardanoGraphs/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('cardanoGraphs/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('cardanoGraphs/litecoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('cardanoGraphs/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('cardanoGraphs/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('cardanoGraphs/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),

    #CARDANO HISTORY TO GRAPH
    path('cardanoHistory/bitcoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('cardanoHistory/cardanoGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('cardanoHistory/dogeGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('cardanoHistory/ethereumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('cardanoHistory/heliumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('cardanoHistory/litecoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('cardanoHistory/polkadotGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('cardanoHistory/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('cardanoHistory/tetherGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),

    #CARDANO HISTORY TO HISTORY
    path('cardanoHistory/bitcoinHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('cardanoHistory/cardanoHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('cardanoHistory/dogeHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('cardanoHistory/ethereumHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('cardanoHistory/heliumHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('cardanoHistory/litecoinHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('cardanoHistory/polkadotHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('cardanoHistory/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    path('cardanoHistory/shibainuHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('cardanoHistory/tetherHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),


    ###########################################DOGE########################################################
    #DOGE GRAPH TO GRAPH
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

    #DOGE GRAPH TO HISTORY
    path('dogeGraphs/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('dogeGraphs/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('dogeGraphs/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('dogeGraphs/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('dogeGraphs/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('dogeGraphs/litecoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('dogeGraphs/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('dogeGraphs/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('dogeGraphs/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),

    #DOGE HISTORY TO GRAPH
    path('dogeHistory/bitcoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('dogeHistory/cardanoGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('dogeHistory/dogeGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('dogeHistory/ethereumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('dogeHistory/heliumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('dogeHistory/litecoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('dogeHistory/polkadotGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('dogeHistory/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('dogeHistory/tetherGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),

    #DOGE TO HISTORY TO HISTORY
    path('dogeHistory/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('dogeHistory/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('dogeHistory/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('dogeHistory/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('dogeHistory/heliumHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('dogeHistory/litecoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('dogeHistory/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('dogeHistory/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('dogeHistory/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('dogeHistory/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),


    ##########################################ETHEREUM############################################
    #ETHEREUM GRAPH TO GRAPH
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

    #ETHEREUM GRAPH TO HISTORY
    path('ethereumGraphs/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('ethereumGraphs/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('ethereumGraphs/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('ethereumGraphs/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('ethereumGraphs/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('ethereumGraphs/litecoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('ethereumGraphs/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('ethereumGraphs/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('ethereumGraphs/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),

    #ETHEREUM HISTORY TO GRAPH
    path('ethereumHistory/bitcoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('ethereumHistory/cardanoGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('ethereumHistory/dogeGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('ethereumHistory/ethereumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs')),
    path('ethereumHistory/heliumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('ethereumHistory/litecoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('ethereumHistory/polkadotGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('ethereumHistory/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('ethereumHistory/tetherGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),

    #ETHEREUM HISTORY TO HISTORY
    path('ethereumHistory/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('ethereumHistory/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('ethereumHistory/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('ethereumHistory/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory')),
    path('ethereumHistory/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('ethereumHistory/litecoinHistory/', RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('ethereumHistory/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('ethereumHistory/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('ethereumHistory/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),
    path('ethereumHistory/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),


    ##############################################HELIUM#################################################
    #HELIUM GRAPH TO GRAPH
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
    
    #HELIUM GRAPH TO HISTORY
    path('heliumGraphs/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('heliumGraphs/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('heliumGraphs/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('heliumGraphs/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('heliumGraphs/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('heliumGraphs/litecoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('heliumGraphs/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('heliumGraphs/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('heliumGraphs/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),

    #HELIUM HISTORY TO GRAPH
    path('heliumHistory/bitcoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('heliumHistory/cardanoGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('heliumHistory/dogeGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('heliumHistory/ethereumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('heliumHistory/heliumGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('heliumHistory/litecoinGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('heliumHistory/polkadotGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('heliumHistory/shibainuGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('heliumHistory/tetherGraphs/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('heliumHistory/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),

    #HELIUM HISTORY TO HISTORY
    path('heliumHistory/bitcoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('heliumHistory/cardanoHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('heliumHistory/dogeHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('heliumHistory/ethereumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('heliumHistory/heliumHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('heliumHistory/litecoinHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('heliumHistory/polkadotHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('heliumHistory/shibainuHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('heliumHistory/tetherHistory/',RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),


    #########################################LITECOIN######################################################
    #LITECOIN GRAPH TO GRAPH
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

    #LITECOIN GRAPH TO HISTORY
    path('litecoinGraphs/bitcoinHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinHistory/')),
    path('litecoinGraphs/cardanoHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/cardanoHistory/')),
    path('litecoinGraphs/dogeHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/dogeHistory/')),
    path('litecoinGraphs/ethereumHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/ethereumHistory/')),
    path('litecoinGraphs/heliumHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/heliumHistory/')),
    path('litecoinGraphs/litecoinHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/litecoinHistory/')),
    path('litecoinGraphs/polkadotHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/polkadotHistory/')),
    path('litecoinGraphs/shibainuHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/shibainuHistory/')),
    path('litecoinGraphs/tetherHistory/',
         RedirectView.as_view(url='http://127.0.0.1:8000/tetherHistory/')),
    path('litecoinGraphs/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),

    #LITECOIN HISTORY TO GRAPH
    path('litecoinHistory/bitcoinGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/bitcoinGraphs/')),
    path('litecoinHistory/cardanoGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/cardanoGraphs/')),
    path('litecoinHistory/dogeGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/dogeGraphs/')),
    path('litecoinHistory/ethereumGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/ethereumGraphs/')),
    path('litecoinHistory/heliumGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/heliumGraphs/')),
    path('litecoinHistory/litecoinGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/litecoinGraphs/')),
    path('litecoinHistory/polkadotGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/polkadotGraphs/')),
    path('litecoinHistory/shibainuGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/shibainuGraphs/')),
    path('litecoinHistory/tetherGraphs/',
         RedirectView.as_view(url='http://127.0.0.1:8000/tetherGraphs/')),
    path('litecoinHistory/home/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    
    #LITECOIN HISTORY TO HISTORY
    
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
