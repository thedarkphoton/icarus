from django.http import request
from sklearn.externals import joblib
import json

titles = ['front_bumber','rear_bumper','left_side','right_side','fl_lights','fr_lights','rl_lights','rr_lights','front_windshield','rear_windshield','roof','fire']

def predict(data):

    #data = json.loads(request.POST.get('data'))

    formattedArray = []

    for idx, val in enumerate(titles):
        name = titles.get(idx)
        data = data.get(name)
        formattedArray.append(data, '')
        print(data)

    clf = joblib.load('treeClassifier_model.pkl')
    prediction = clf.predict([formattedArray])
    print prediction
    return prediction

predict()