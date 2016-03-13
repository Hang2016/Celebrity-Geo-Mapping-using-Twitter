'''
Created on Mar 12, 2016

@author: Chen
'''
#using tweepy library
import tweepy

# initialize Twitter API variables
consumer_key ="kEVacgboUkLbbmPHDy2DvIKNS"
consumer_secret ="2GzJh4RlP1h0ey4Y8SrfESCne0KqtTIhcAXGeCqaQcK1hCIyX0"
access_token="4855734711-D0BC8lU0HMGQEEdbqQyzF2CaJvESvMOLQUwZDys"
access_token_secret="PdB23ZFiiQWOSC3JJOpiZ6O4c1DEqFTYtpJq2WllyiOj2"

#Authenticate Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get the name and twitter id of each celebrity in the text file.
def getCelebrities(filename):
    with open(filename) as f:
        for line in f:
            name = line.split(":")[0]
            print "name == " + name
            twitterID = line.split(":")[1]#get twitter ID from file
            print "twitter id == " + twitterID
            getCelebrityTweets(twitterID)

#get the most recent 20 tweets of each celebrity            
def getCelebrityTweets(twitterID):
    tweets = api.user_timeline(id=twitterID)
    for tweet in tweets:
        getTweetAndLocation(tweet)

#get tweet text and location data of a tweet        
def getTweetAndLocation(tweet):
    print "tweet text == " + tweet.text
    place = tweet.place
    #check if the tweet contains location data
    if(place != None):
        print "place == " + place.full_name
        print "coordinate==",
        print place.bounding_box.coordinates
    else:
        print "No Location Info"
        
getCelebrities("test.txt")