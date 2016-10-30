from sklearn.externals import joblib
import os.path
import predicter

titles = ['front_bumber','rear_bumper','left_side','right_side','fl_lights','fr_lights','rl_lights','rr_lights','front_windshield','rear_windshield','roof','fire']

def predict(data):

    formattedArray = []

    for idx, val in enumerate(titles):
        value = 0
        if (val in data.itervalues()):
            value = data.get(val)
        formattedArray.append(value)
    print(formattedArray)

    clf = joblib.load('treeClassifier_model.pkl')
    prediction = clf.predict([formattedArray])
    print prediction
    return prediction