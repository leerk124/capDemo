from django.shortcuts import render
from django.http import HttpResponse
import PlotlyTest

#HOMEPAGE
def home(requests):
    return render(requests, 'home/welcome.html')

#GRAPH PAGES
def bitcoinGraphs(requests):
    graph_html_list = PlotlyTest.main('bitcoin')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/bitcoinGraphs.html', context)

def cardanoGraphs(requests):
    graph_html_list = PlotlyTest.main('cardano')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/cardanoGraphs.html', context)

def dogeGraphs(requests):
    graph_html_list = PlotlyTest.main('doge')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/dogeGraphs.html', context)

def ethereumGraphs(requests):
    graph_html_list = PlotlyTest.main('ethereum')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/ethereumGraphs.html', context)

def heliumGraphs(requests):
    graph_html_list = PlotlyTest.main('helium')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/heliumGraphs.html', context)

def litecoinGraphs(requests):
    graph_html_list = PlotlyTest.main('litecoin')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/litecoinGraphs.html', context)

def polkadotGraphs(requests):
    graph_html_list = PlotlyTest.main('polkadot')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/polkadotGraphs.html', context)

def shibainuGraphs(requests):
    graph_html_list = PlotlyTest.main('shibainu')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/shibainuGraphs.html', context)

def tetherGraphs(requests):
    graph_html_list = PlotlyTest.main('tether')
    context = {'candleStick_Graph': graph_html_list[0],
               'volume': graph_html_list[1]}
    return render(requests, 'home/tetherGraphs.html', context)
