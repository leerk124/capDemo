from django.urls import path
from .import views  # import our views in this folder too

urlpatterns = [

    #call the url home
    #point at the views.py file in our home folder
    path('', views.home, name='home'),
    path('bitcoin/', views.bitcoin, name='bitcoin'),
    ]

#connect everything to our master url.py (aka cap urls.py)
