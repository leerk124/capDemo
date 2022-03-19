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
