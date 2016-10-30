from django.http import request
from sklearn.externals import joblib
import json

titles = ['front_bumber','rear_bumper','left_side','right_side','fl_lights','fr_lights','rl_lights','rr_lights','front_windshield','rear_windshield','roof','fire']

def predict(data):

    #data = json.loads(request.POST.get('data'))

    # formattedArray = []

    # for name in titles:
    #     value = 0
    #     if name in data :
    #         value = data[name]
    #     formattedArray.append(value)
    
    # print(formattedArray)

    # clf = joblib.load('treeClassifier_model.pkl')
    # prediction = clf.predict([formattedArray])
    # print prediction
    # return prediction

    return "your car is severely damaged and will need to be written off. Don't worry we can arrange a cash lump some to be paid out to you."
