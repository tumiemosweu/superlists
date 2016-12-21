from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse
#from django.views.generic import FormView
# Create your views here.

class HomePageView():
    
    def home_page(self,request):
        return HttpResponse()