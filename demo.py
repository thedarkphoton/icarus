from sklearn import tree

clf = tree.DecisionTreeClassifier()

# front bumber, right side, rear bumper, left side, rear lights, rear windshield, front windshield, wheels, roof , fire

X = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1,0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1,0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0,0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0,0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0,0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0,0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0,0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0,0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0,0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0,0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    ]

Y = ['write-off', 'write-off', 'write-off', 'write-off', 'write-off', 'write-off','write-off', 'write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off','not-write-off']

clf = clf.fit(X, Y)

prediction = clf.predict([ [0, 0, 1, 0, 1, 0, 0, 1, 0, 0]])

print prediction