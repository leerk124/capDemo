from django.shortcuts import render
from django.http import HttpResponse
import PlotlyTest

# Create your views here.

def home(requests):
    return render(requests, 'home/welcome.html')

def bitcoin(requests):
    graph_html_list = PlotlyTest.main('bitcoin')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/bitcoin.html', context)

def cardano(requests):
    graph_html_list = PlotlyTest.main('cardano')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/cardano.html', context)

def doge(requests):
    graph_html_list = PlotlyTest.main('doge')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/doge.html', context)

def ethereum(requests):
    graph_html_list = PlotlyTest.main('ethereum')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/ethereum.html', context)

def helium(requests):
    graph_html_list = PlotlyTest.main('helium')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/helium.html', context)

def litecoin(requests):
    graph_html_list = PlotlyTest.main('litecoin')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/litecoin.html', context)

def polkadot(requests):
    graph_html_list = PlotlyTest.main('polkadot')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/polkadot.html', context)

def shibainu(requests):
    graph_html_list = PlotlyTest.main('shibainu')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/shibainu.html', context)

def tether(requests):
    graph_html_list = PlotlyTest.main('tether')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/tether.html', context)
