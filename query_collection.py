# William Dahl
# 001273655
# ICSI 431 - Data Mining

import tweepy, sys

reload(sys)
sys.setdefaultencoding("utf-8")

OAuth = tweepy.OAuthHandler('PeH7lROp4ihy4QyK87FZg', '1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og')
OAuth.set_access_token('1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7', 'e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw')
myApi = tweepy.API(OAuth)
f = open("unlabeled_queries.txt", "w")

def query1():
	geo = "42.6529,-73.7562,50.00mi"
	query = "traffic AND Albany"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query2():
	geo = "42.6529,-73.7562,50.00mi"
	query = "car accident AND Albany"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query3():
	geo = "42.6529,-73.7562,50.00mi"
	query = "traffic AND Washington Ave"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query4():
	geo = "42.6529,-73.7562,50.00mi"
	query = "traffic AND Western Ave"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query5():
	geo = "42.6529,-73.7562,50.00mi"
	query = "traffic AND Central Ave"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")


def query6():
	geo = "42.6529,-73.7562,50.00mi"
	query = "accident AND Central Ave"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query7():
	geo = "42.6529,-73.7562,50.00mi"
	query = "accident AND Washington Ave"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query8():
	geo = "42.6529,-73.7562,50.00mi"
	query = "accident AND Western Ave"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query9():
	geo = "42.6529,-73.7562,50.00mi"
	query = "accident AND I-90 AND Albany"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query10():
	geo = "42.6529,-73.7562,50.00mi"
	query = "traffic AND I-90 AND Albany"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query11():
	geo = "42.6529,-73.7562,50.00mi"
	query = "traffic AND CDTA"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

def query12():
	geo = "42.6529,-73.7562,50.00mi"
	query = "accident AND CDTA"
	tweets = myApi.search(q=query, geocode=geo, count=100)
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")

if __name__ == '__main__':
	query1()
	query2()
	query3()
	query4()
	query5()
	query6()
	query7()
	query8()
	query9()
	query10()
