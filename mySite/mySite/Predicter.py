from django.http import request
from sklearn.externals import joblib
import json

titles = ['front_bumber','rear_bumper','left_side','right_side','fl_lights','fr_lights','rl_lights','rr_lights','front_windshield','rear_windshield','roof','fire']

def predict(data):

    clf = joblib.load('treeClassifier_model.pkl')
    predication = clf.predict(data)

<<<<<<< HEAD
    formattedArray = []

    for name in titles:
        value = 0
        if name in data :
            value = data[name]
        formattedArray.append(value)
    
    print(formattedArray)

    clf = joblib.load('treeClassifier_model.pkl')
    prediction = clf.predict([formattedArray])
    print prediction
    return prediction

    # return "Done something"
=======
    print predication
    return predication
>>>>>>> 37580a3472014129189f1294ee9d45781f5c474f
