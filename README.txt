Modules:
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from Tkinter import *
import warnings
import re
import tweepy, sys
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

Instructions To Run:
code can be runin py charm using the run function.
Or you can run in command line using python ./<file_name.py>

First you want to run query_collection.py. This will Generate a text file called unlabeled_queries.txt

Then run SVM_model.py. This will generate a text file called predicted tweets. Make sure you have the trining data in the same directory when you run SVM_model.py called training_set.txt

The run the classification.py code and experince our app. You can choose to plan your commute via road to time. Wich ever you choose uts enter the HOUR you would like to leave, or the road you would like to travel on. Then either exit the program by clicking exit, or choose to enter in a new time or road.

File Discriptions:
The data set is called queries.txt. The trainig set used in SVM_model is called training_set.txt. Make sure you have both of these. 

query_collection.py: collectes tweets from twitter using a REST API and stroes them in a file called unlabeled_queries.txt

SVM_model.py: uses the traing data in the file training_set.txt to predict the truth value for the tweets in the file unlabeled_queries.txt. It then stores those predicited tweets in to a file called predicted_queries.txt. Then writes the tweets that were predicted to be true to the queries data set.

classification.py: uses the data set in queries to predict how conjested the traffic will be on a road at a certian time. It askes the user to choose how they would like to plan their commute. The user can then choose "By Time" or "By Road" and then enter the HOUR they would like to leave or the road that they would like to travel on, respectivly. The program then out put the times if the user choose "By road" or the road if the user chose "By time" in order form least likly to be conjested to most likly to be conjested.

