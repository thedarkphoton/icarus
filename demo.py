from sklearn import tree, svm
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.externals import joblib

treeClassifier = tree.DecisionTreeClassifier()
linearSVC = LinearSVC()
svc = svm.SVC()

titles = ['front_bumber','rear_bumper','left_side','right_side','fl_lights','fr_lights','rl_lights','rr_lights','front_windshield','rear_windshield','roof','fire']

#Spaced every 10 for counting purposes
#Damage: 0 = no , 1 = medium, 2 = high
X = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
    [2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],

    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0],

    [1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
    [1, 0, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0],

]

#Spaced every 5 for counting purposes~
Y = [
    'write-off', 'write-off', 'write-off', 'write-off', 'write-off',
    'write-off', 'write-off', 'write-off', 'write-off', 'write-off',
    'write-off', 'write-off', 'write-off', 'write-off', 'write-off',
    'write-off', 'write-off', 'write-off', 'write-off', 'write-off',
    'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off',
    'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off',
    'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off',
    'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off',
    'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off',
    'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off', 'not-write-off',
]

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.4, random_state=1)

param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }

svc = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)

# This is the Server-side code to decide which classifier is best
# Use the linearSVC_model as it is the best. Tested for different values of C and Gamma, and changing training set size.
treeClassifier_model = treeClassifier.fit(X_train, y_train)
svc_model = svc.fit(X_train,y_train)
linearSVC_model = linearSVC.fit(X_train, y_train)

print 'TreeClassifier:'
print treeClassifier_model.score(X_test, y_test)
print 'SVC:'
print svc_model.score(X_test, y_test)
print svc_model.best_params_
print '-------------'
print 'LinearSVC'
print linearSVC_model.score(X_test, y_test)

#reconstruction
y_pred = svc.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['not-write-off','write-off']))

# API has only 1 get method which uses the LinearSVC classifier variable to call treeClassifier_model.predict(input from website)
print treeClassifier_model.predict([[0,0,0,0,0,0,0,0,0,1,0,0]])

#Save model to file
joblib.dump(treeClassifier_model, 'treeClassifier_model.pkl')



#Load and predict
predict()


