from sklearn import tree, svm
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

treeClassifier = tree.DecisionTreeClassifier()
linearSVC = LinearSVC()
svc = svm.SVC()

# front bumber, right side, rear bumper, left side, rear lights, rear windshield, front windshield, wheels, roof , fire
titles = ['bumber','right side','rear bumper','left side','rear lights','rear windshield','front windshield','wheels','roof','fire']

#Spaced every 10 for counting purposes
X = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],

    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],

    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 0],

    ]

#Spaced every 5 for counting purposes~
Y = [
    'write-off', 'write-off', 'write-off', 'write-off', 'write-off',
    'write-off','write-off', 'write-off','not-write-off','not-write-off',
    'not-write-off','not-write-off','not-write-off','not-write-off','not-write-off',
    'not-write-off','not-write-off','not-write-off','not-write-off','not-write-off',
    'write-off', 'write-off', 'write-off', 'write-off', 'write-off',
    'write-off', 'write-off', 'write-off', 'write-off', 'write-off',
]

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.30, random_state=1)

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


# API has only 1 get method which uses the LinearSVC classifier variable to call linearSVC.predict(input from website)
print linearSVC.predict([[0,0,0,0,0,0,0,0,0,1]])


