from django.http import request
from sklearn.externals import joblib
import json

titles = ['front_bumber','rear_bumper','left_side','right_side','fl_lights','fr_lights','rl_lights','rr_lights','front_windshield','rear_windshield','roof','fire']

def predict(data):

    clf = joblib.load('treeClassifier_model.pkl')
    predication = clf.predict(data)

    print predication
    return predication
