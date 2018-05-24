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
warnings.filterwarnings("ignore")

class Route:
	def __init__(self, new_name):
		self.count = 0
		self.name = new_name

	def avg(self, num_tweets):
		if num_tweets == 0:
			self.avg = 0

		else:
			self.avg = self.count/num_tweets

class Time:
	def __init__(self, time):
		self.count = 0
		self.time = time

	def avg(self, num_tweets):
		if num_tweets == 0:
			self.avg = 0

		else:
			self.avg = self.count/num_tweets

def enter_time():
	global e
	global var
	entry = Tk()
	entry.title("Enter Time")
	label = Label(entry, text='Enter the hour you want to leave')
	label.pack(side='top')
	e = Entry(entry)
	e.pack()
	e.focus_set()
	b = Button(entry, text='enter', command=get_time)
	b.pack(side='bottom')
	entry.mainloop()

def get_time():
	global e
	global time
	global var
	time = e.get()
	time_class()

def time_class():
	global time
	i90 = Route("I-90")
	i87 = Route("I-87")
	i787 = Route("I-787")
	central = Route("Central Ave")
	washington = Route("Washington Ave")
	western = Route("Western Ave")
	madison = Route("Madison Ave")
	broadway = Route("Broadway")
	northway= Route("Northway")
	tweets = []
	for line in open("queries.txt").readlines():
		if time == line[14]:
			tweets.append(line)

		else:
			hour = line[13] + line[14]
			if hour == time:
				tweets.append(line)

	for tweet in tweets:
		if "I-90" in tweet:
			i90.count += 1

		if "I-87" in tweet:
			i87.count += 1

		if "I-787" in tweet:
			i787.count += 1

		if "Central Ave" in tweet:
			central.count += 1

		if "Washington Ave" in tweet: 
			washington.count += 1

		if "Western Ave" in tweet:
			western.count += 1

		if "Madison Ave" in tweet:
			madison.count += 1

		if "Broadway" in tweet:
			broadway.count += 1

		if "Northway" in tweet:
			northway.count += 1

	i90.avg(len(tweets))
	i87.avg(len(tweets))
	i787.avg(len(tweets))
	central.avg(len(tweets))
	washington.avg(len(tweets))
	madison.avg(len(tweets))
	broadway.avg(len(tweets))
	western.avg(len(tweets))
	northway.avg(len(tweets))

	routes = [i90, i87, i787, central, washington, madison, broadway, northway]
	routes.sort(key=lambda x: x.count)
	print_routes(routes)

def print_routes(routes):
	message = Tk()
	message.title("Routes")
	label = Label(message, text="Best Routes to Take in Order") 
	label.config(font=(18))
	label.pack(side="top")
	label = Label(message, text="Best", fg='green')
	label.pack()
	for route in routes:
		if route.avg < .25:
			label = Label(message, text = route.name)
			label.pack()

		else:
			label = Label(message, text = route.name)
			label.pack()

	label = Label(message, text = "Worst", fg='red')
	label.pack()
	button = Button(message, text='Enter New Time', command=enter_time)
	button.pack(side=LEFT)
	button = Button(message, text='Exit', command=quit)
	button.pack(side=LEFT)
	button = Button(message, text='By Road', command=enter_road)
	button.pack(side=LEFT)
	message.mainloop()

def enter_road():
	global e
	entry = Tk()
	entry.title("Enter Road")
	label = Label(entry, text='Enter the road you would like to take')
	label.pack(side='top')
	e = Entry(entry)
	e.pack()
	e.focus_set()
	b = Button(entry, text='enter', command=get_road)
	b.pack(side='bottom')
	entry.mainloop()

def get_road():
	global e
	global road
	road = e.get()
	road_class()

def road_class():
	global road
	zero = Time("12:00 AM")
	one = Time("1:00 AM")
	two = Time("2:00 AM")
	three = Time("3:00 AM")
	four = Time("4:00 AM")
	five = Time("5:00 AM")
	six = Time("6:00 AM")
	seven = Time("7:00 AM")
	eight = Time("8:00 AM")
	nine = Time("9:00 AM")
	ten = Time("10:00 AM")
	eleven = Time("11:00 AM")
	twelve = Time("12:00 PM")
	thirteen = Time("1:00 PM")
	fourteen = Time("2:00 PM")
	fifteen = Time("3:00 PM")
	sixteen = Time("4:00 PM")
	seventeen = Time("5:00 PM")
	eightteen = Time("6:00 PM")
	nineteen = Time("7:00 PM")
	twenty = Time("8:00 PM")
	twentyOne = Time("9:00 PM")
	twentyTwo = Time("10:00 PM")
	twentyThree = Time("11:00 PM")
	tweets = []
	for line in open("queries.txt").readlines():
		if road in line:
			tweets.append(line)

	for tweet in tweets:
		if tweet[13] == "0":
			time = tweet[14]
			if time == "0":
				zero.count += 1

			if time == "1":
				one.count += 1

			if time == "2":
				two.count += 1

			if time == "3":
				three.count += 1

			if time == "4":
				four.count += 1

			if time == "5":
				five.count += 1

			if time == "6":
				six.count += 1

			if time == "7":
				seven.count += 1

			if time == "8":
				eight.count += 1

			if time == "9":
				nine.count += 1

		else:
			time = tweet[13] + tweet[14]
			if time == "10":
				ten.count += 1

			if time == "11":
				eleven.count += 1

			if time == "12":
				twelve.count += 1

			if time == "13":
				thirteen.count += 1

			if time == "14":
				fourteen.count += 1

			if time == "15":
				fifteen.count += 1

			if time == "16":
				sixteen.count += 1

			if time == "17":
				seventeen.count += 1

			if time == "18":
				eightteen.count += 1

			if time == "19":
				nineteen.count += 1

			if time == "20":
				twenty.count += 1

			if time == "21":
				twentyOne.count += 1

			if time == "22":
				twentyTwo.count += 1

			if time == "23":
				twentyThree.count += 1

	zero.avg(len(tweets))
	one.avg(len(tweets))
	two.avg(len(tweets))
	three.avg(len(tweets))
	four.avg(len(tweets))
	five.avg(len(tweets))
	six.avg(len(tweets))
	seven.avg(len(tweets))
	eight.avg(len(tweets))
	nine.avg(len(tweets))
	ten.avg(len(tweets))
	eleven.avg(len(tweets))
	twelve.avg(len(tweets))
	thirteen.avg(len(tweets))
	fourteen.avg(len(tweets))
	fifteen.avg(len(tweets))
	sixteen.avg(len(tweets))
	seventeen.avg(len(tweets))
	eightteen.avg(len(tweets))
	nineteen.avg(len(tweets))
	twenty.avg(len(tweets))
	twentyOne.avg(len(tweets))
	twentyTwo.avg(len(tweets))
	twentyThree.avg(len(tweets))

	times = [zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eightteen, nineteen, twenty, twentyOne, twentyTwo, twentyThree]
	times.sort(key=lambda x: x.count)
	print_times(times)

def print_times(times):
	message = Tk()
	message.title("Times")
	label = Label(message, text="The best times to use that road are")
	label.config(font=(18))
	label.pack(side="top")
	label = Label(message, text="Best", fg='green')
	label.pack()
	for time in times:
		if time.avg < .25:
			label = Label(message, text = time.time)
			label.pack()

		else:
			label = Label(message, text = time.time)
			label.pack()

	label = Label(message, text = "Worst", fg='red')
	label.pack()
	button = Button(message, text='Enter New Road', command=enter_road)
	button.pack(side=LEFT)
	button = Button(message, text='Exit', command=quit)
	button.pack(side=LEFT)
	button = Button(message, text='By Time', command=enter_time)
	button.pack(side=LEFT)
	message.mainloop()

root = Tk()
root.title("Plan Your Commute")
label = Label(root, text='Choose how you would like to plan your Commute')
label.pack(side='top')
b = Button(root, text='By Time',command=enter_time)
b.pack(side=LEFT)
b = Button(root, text='By Road', command=enter_road)
b.pack(side=LEFT)
b = Button(root, text='Exit', command=quit)
b.pack(side=LEFT)
root.mainloop()