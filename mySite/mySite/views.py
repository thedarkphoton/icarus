from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import json

# Create your views here.
def sendData(request):
    if request.method == 'POST':
    	myDict = dict(request.POST.iterlists())
    	print myDict
        
    return HttpResponse("Got it!")
