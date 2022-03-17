from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#push test

def home(requests):
    #return our html templates
    #(in order for it to show up we need to go to settings => installed apps)
    return render(requests, 'home/welcome.html')


def bitcoin(requests):
    return render(requests,'home/bitcoin.html')


# #takes us to sample coin page
# def bitcoin(requests):
#     return HttpResponse('Bitcoin')
