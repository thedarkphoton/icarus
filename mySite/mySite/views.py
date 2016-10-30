from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import json

# Create your views here.
import Predicter

#titles = ['front_bumber','rear_bumper','left_side','right_side','fl_lights','fr_lights','rl_lights','rr_lights','front_windshield','rear_windshield','roof','fire']


def sendData(request):
<<<<<<< HEAD
    if request.method == 'POST':
        myDict = dict(request.POST.iterlists())
        output = Predicter.predict(myDict)
        return HttpResponse(output)
        # myData = ast.literal_eval(request.body)
        # print myData
        # print myData["info"]
    return HttpResponse("Error")
=======

    # if request.method == 'POST':
    #     myDict = dict(request.POST.iterlists())
    #     Predicter.predict(myDict)
    #     print myDict
    #     # myData = ast.literal_eval(request.body)
    #     # print myData
    #     # print myData["info"]
    # predict([request.POST[:]])

    data = [0,0,0,0,0,0,0,0,0,0,0,0]
    data[0] = 0 if request.POST["claim_front"] == None else int(request.POST["claim_front"]);
    data[1] = 0 if request.POST["claim_back"] == None else int(request.POST["claim_back"]);
    data[2] = 0 if request.POST["claim_passenger_side"] == None else int(request.POST["claim_passenger_side"]);
    data[3] = 0 if request.POST["claim_driver_side"] == None else int(request.POST["claim_driver_side"]);
    data[4] = 0 if request.POST["claim_fl_light"] == None else int(request.POST["claim_fl_light"]);
    data[5] = 0 if request.POST["claim_fr_light"] == None else int(request.POST["claim_fr_light"]);
    data[6] = 0 if request.POST["claim_bl_light"] == None else int(request.POST["claim_bl_light"]);
    data[7] = 0 if request.POST["claim_br_light"] == None else int(request.POST["claim_br_light"]);
    data[8] = 0 if request.POST["claim_front_windscreen"] == None else int(request.POST["claim_front_windscreen"]);
    data[9] = 0 if request.POST["claim_back_windscreen"] == None else int(request.POST["claim_back_windscreen"]);
    data[10] = 0 if request.POST["claim_roof"] == None else int(request.POST["claim_roof"]);
    data[11] = 0 if request.POST["claim_fire"] == None else int(request.POST["claim_fire"]);

    return HttpResponse(Predicter.predict(data))
>>>>>>> 37580a3472014129189f1294ee9d45781f5c474f
