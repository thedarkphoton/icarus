from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def sendData(request):
    print 'RECEIVED REQUEST: ' + request.method
    if request.method == 'POST':
        print 'Hello'
    return HttpResponse("Got it!")
