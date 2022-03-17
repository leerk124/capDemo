from django.shortcuts import render
from django.http import HttpResponse
import PlotlyTest

# Create your views here.

def home(requests):
    # graph = PlotlyTest.main('bitcoin')
    return render(requests, 'home/welcome.html', PlotlyTest.main('bitcoin'))


def bitcoin(requests):
    return render(requests,'home/bitcoin.html')
