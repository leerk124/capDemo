from django.shortcuts import render
from django.http import HttpResponse
import PlotlyTest

# Create your views here.

def home(requests):
    return render(requests, 'home/welcome.html')

def bitcoinGraphs(requests):
    graph_html_list = PlotlyTest.main('bitcoinGraphs')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/bitcoinGraphs.html', context)

def cardano(requests):
    graph_html_list = PlotlyTest.main('cardano')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/cardanoGraphs.html', context)

def doge(requests):
    graph_html_list = PlotlyTest.main('doge')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/dogeGraphs.html', context)

def ethereum(requests):
    graph_html_list = PlotlyTest.main('ethereum')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/ethereumGraphs.html', context)

def helium(requests):
    graph_html_list = PlotlyTest.main('helium')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/heliumGraphs.html', context)

def litecoin(requests):
    graph_html_list = PlotlyTest.main('litecoin')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/litecoinGraphs.html', context)

def polkadot(requests):
    graph_html_list = PlotlyTest.main('polkadot')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/polkadotGraphs.html', context)

def shibainu(requests):
    graph_html_list = PlotlyTest.main('shibainu')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/shibainuGraphs.html', context)

def tether(requests):
    graph_html_list = PlotlyTest.main('tether')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/tetherGraphs.html', context)
