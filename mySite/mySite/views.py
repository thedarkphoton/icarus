from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import json

# Create your views here.
from mySite import Predicter

def sendData(request):
    if request.method == 'POST':
        myDict = dict(request.POST.iterlists())
        Predicter.predict(myDict)
        print myDict
        # myData = ast.literal_eval(request.body)
        # print myData
        # print myData["info"]

    return HttpResponse("Got it!")
