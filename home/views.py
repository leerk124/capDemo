from django.shortcuts import render
import PlotlyTest

# Create your views here.
# push test

def home(requests):
    graph = PlotlyTest.main('bitcoin')
    return render(requests, 'home/welcome.html', graph)