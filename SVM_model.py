#William Dahl
#ICSI 431 Data Mining
#April 11th, 2018

import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

x = [[0 for i in range(10)] for j in range(len(open("queries.txt", "r").readlines()))] #2d array holding frecuncy of words in tweets
y = [0 for i in range(len(open("queries.txt", "r").readlines()))] #total frecuncy of each tweet
#opens the file for reading
with open("training_set.txt", "r") as f:
	#loops through the 500 tweets
	for i in range(len(open("training_set.txt", "r").readlines())):
		line = f.readline().lower()#line read 
		y[i] = int(line[0])
		#checks if one of the 10 words apearing the tweet
		if "traffic" in line:
			x[i][0] = 1
		if "totaltrafficalb" in line:
			x[i][1] = 1
		if "accident" in line:
			x[i][2] = 1
		if "albany" in line:
			x[i][3] = 1
		if "exit" in line:
			x[i][4] = 1
		if "blocked" in line:
			x[i][5] = 1
		if "shoulder" in line:
			x[i][6] = 1
		if "cleared" in line:
			x[i][7] = 1
		if "northway" in line:
			x[i][8] = 1
		if "right" in line:
			x[i][9] = 1 

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, x, y, cv=10)


tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
scores = ['precision', 'recall']
svr = svm.SVC(C=1)
for score in scores:
    clf = GridSearchCV(svr, tuned_parameters, cv=10,scoring='%s_macro'% score)
    clf.fit(x, y)
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']

x_test = [[0 for i in range(10)] for j in range(len(open("unlabeled_queries.txt", "r").readlines()))] #2d array holding frecuncy of words in tweets
y_test = [0 for i in range(len(open("unlabeled_queries.txt", "r").readlines()))] #total frecuncy of each tweet
#opens the file for reading
with open("unlabeled_queries.txt", "r") as f:
	#loops through the 500 tweets
	for i in range(len(open("unlabeled_queries.txt", "r").readlines())):
		vector_sum = 0 #frecuency total
		line = f.readline().lower()#line read 
		#checks if one of the 10 words apears in the tweet
		if "traffic" in line:
			x_test[i][0] = 1
		if "totaltrafficalb" in line:
			x_test[i][1] = 1
		if "accident" in line:
			x_test[i][2] = 1
		if "albany" in line:
			x_test[i][3] = 1
		if "exit" in line:
			x_test[i][4] = 1
		if "blocked" in line:
			x_test[i][5] = 1
		if "shoulder" in line:
			x_test[i][6] = 1
		if "cleared" in line:
			x_test[i][7] = 1
		if "northway" in line:
			x_test[i][8] = 1
		if "right" in line:
			x_test[i][9] = 1 

for score in scores:
	y_pred = clf.predict(x_test)

p = open("predicted_tweets.txt", "w")
with open("unlabeled_queries.txt", "r") as f:
	for i in range(len(open("unlabeled_queries.txt", "r").readlines())):
		line = f.readline()
		if y_pred[i] == 0:
			line = "0 " + line
		else:
			line = "1 " + line

		p.write(line)


p = open("predicted_tweets.txt", "r")
g = open("queries.txt", "a")
for line in p.readlines():
	if line[0] == "1":
		g.write(line)
