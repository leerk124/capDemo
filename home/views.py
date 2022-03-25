from django.shortcuts import render
from django.http import HttpResponse
import PlotlyTest

# Create your views here.

def home(requests):
    return render(requests, 'home/welcome.html')

def bitcoin(requests):
    divTEST = PlotlyTest.main('bitcoin')
    context = {'graph': divTEST}
    return render(requests, 'home/bitcoin.html', context)

def cardano(requests):
    return render(requests, 'home/cardano.html')

def doge(requests):
    return render(requests, 'home/doge.html')

def ethereum(requests):
    return render(requests, 'home/ethereum.html')


def helium(requests):
    return render(requests, 'home/helium.html')


def litecoin(requests):
    return render(requests, 'home/litecoin.html')


def polkadot(requests):
    return render(requests, 'home/polkadot.html')


def shibainu(requests):
    return render(requests, 'home/shibainu.html')


def tether(requests):
    return render(requests, 'home/tether.html')
