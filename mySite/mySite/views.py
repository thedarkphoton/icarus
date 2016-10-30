from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import ast

# Create your views here.
def sendData(request):
    if request.method == 'POST':
        print request.body
        # myData = ast.literal_eval(request.body)
        # print myData
        # print myData["info"]
    return HttpResponse("Got it!")
