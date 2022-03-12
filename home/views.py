from django.shortcuts import render

# Create your views here.
#push test

def home(requests):
    #return our html templates
    #(in order for it to show up we need to go to settings => installed apps)
    return render(requests, 'home/welcome.html')