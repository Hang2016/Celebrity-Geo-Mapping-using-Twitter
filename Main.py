import tweepy
import json

# initialize Twitter API variables

consumer_key = "kEVacgboUkLbbmPHDy2DvIKNS"
consumer_secret = "2GzJh4RlP1h0ey4Y8SrfESCne0KqtTIhcAXGeCqaQcK1hCIyX0"
access_token = "4855734711-D0BC8lU0HMGQEEdbqQyzF2CaJvESvMOLQUwZDys"
access_token_secret = "PdB23ZFiiQWOSC3JJOpiZ6O4c1DEqFTYtpJq2WllyiOj2"
# Authenticate Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

name = ""
category = ""
tweetContent = ""
countryCode = ""
state = ""
city = ""
latitude = ""
longitude = ""
followersCount = ""
twitterID = ""
time =""

celebrityLists=""
commedian_lists = ""
movie_star_lists = ""
musicians_lists = ""
sport_star_lists=""
reality_tv_internet_lists=""
idLists = ""
testList=""

class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        global twitterID
        global tweetContent
        global city
        global state
        global category
        global name
        global countryCode
        global latitude
        global longitude
        global followersCount
        global time

        twitterID =''
        tweetContent = ''
        city =''
        state =''
        category=''
        name=''
        countryCode=''
        latitude=''
        longitude=''
        followersCount=''
        time=''

        try:
            if decoded['place'] != None:
                twitterID = decoded['user']['screen_name']
                tweetContent = decoded['text']
                fulllocation = str(decoded['place']['full_name'])
                city = fulllocation.split(",")[0]
                state = fulllocation.split(",")[1]
                countryCode = decoded['place']['country_code']
                latitude  = decoded['place']['bounding_box']['coordinates'][0][0][0]
                longitude = decoded['place']['bounding_box']['coordinates'][0][0][1]
                followersCount = decoded['user']['followers_count']
                time = decoded['user']['created_at']
                category = getCategogy(twitterID)
                name = getName(twitterID)

            if (name !='' and category !='' and tweetContent !='' and countryCode!='' and state!='' and city!='' and latitude !='' and longitude !='' and followersCount !='' and twitterID !='' and time!=''):
                print 'true'
                formatJson = {'name': name, 'twitterID': twitterID, 'followersCount': followersCount,
                          'category': category, 'tweetContent': tweetContent, 'time': time,
                          'countryCode': countryCode, 'state': state, 'city': city, 'latitude': latitude,
                          'longitude': longitude}
                with open('results.json', mode='a') as f:
                    json.dump(formatJson, f, indent=2, separators=(',', ':'))
                    f.write(",")
                    f.write("\n")
        except:
            pass
        return True

def getCategogy(id):
    global commedian_lists
    global movie_star_lists
    global musicians_lists
    global sport_star_lists
    global reality_tv_internet_lists
    global testList

    if id in commedian_lists:
        print 'FOUND!'
        return 'Commedian'
    elif id in movie_star_lists:
        print 'FOUND!'
        return 'Movie Star'
    elif id in musicians_lists:
        print 'FOUND!'
        return 'Musician'
    elif id in sport_star_lists:
        print 'FOUND!'
        return 'Sport Star'
    elif id in reality_tv_internet_lists:
        print 'FOUND!'
        return 'TV&Internet Celebrity'
    elif id in testList:
        print 'FOUND!'
        return 'test'
    else:
        return ''

def getName(id):
    file1 = 'sport_stars.txt'
    file2 = 'Comedians.txt'
    file3 ='musicians.txt'
    file4 = 'movie_stars.txt'
    file5 = 'Reality_TV_Internet_Celebrities.txt'
    file6 = 'test2.txt'
    global name
    name = getNameByID(file1,id)
    if name !=None:
        return name
    name = getNameByID(file2,id)
    if name !=None:
        return name
    name = getNameByID(file3,id)
    if name !=None:
        return name
    name = getNameByID(file4,id)
    if name !=None:
        return name
    name = getNameByID(file5,id)
    if name !=None:
        return name
    name = getNameByID(file6,id)
    if name !=None:
        return name

def getNameByID(filename,id):
    with open(filename) as f:
        for line in f:
            if id in line:
                return line.split(":")[0]
def getCelebrities(filename):
    list = ""
    with open(filename) as f:
        for line in f:
            global name
            name = line.split(":")[0]
            global twitterID
            twitterID = line.split(":")[1]
            if list == "":
                list+="\'"
                list+=str(twitterID)
                list+="\'"
            else:
                list+=','
                list+="\'"
                list+=str(twitterID)
                list+="\'"
    return list.replace('\n','')
def getUserIDs(filename):
    global idLists
    with open(filename) as f:
        for line in f:
            if idLists == "":
                idLists+=str(line)
            else:
                idLists+=','
                idLists+=str(line)
def getCategory(name):
    if name in commedian_lists:
        return 'Commedian'
    elif name in movie_star_lists:
        return 'Movie Star'
    elif name in sport_star_lists:
        return 'Sport Star'
    elif name in musicians_lists:
        return 'Musician'
    elif name in reality_tv_internet_lists:
        return 'Reality_TV_Internet'
    else:
        return ''


musicians_lists = getCelebrities('musicians.txt')
movie_star_lists = getCelebrities('movie_stars.txt')
reality_tv_internet_lists = getCelebrities('Reality_TV_Internet_Celebrities.txt')
commedian_lists = getCelebrities('Comedians.txt')
sport_star_lists = getCelebrities('sport_stars.txt')

getUserIDs('Commedians_IDs.txt')
getUserIDs('movie_stars_IDs.txt')
getUserIDs('musicians_IDs.txt')
getUserIDs('reality_tv_internet_celebrities_IDs.txt')
getUserIDs('sport_stars_IDs.txt')


celebrityLists =testList
celebrityLists +=','
celebrityLists += musicians_lists
celebrityLists +=','
celebrityLists +=movie_star_lists
celebrityLists +=','
celebrityLists +=reality_tv_internet_lists
celebrityLists +=','
celebrityLists +=commedian_lists
celebrityLists +=','
celebrityLists +=sport_star_lists


idLists = idLists.replace('\n','')
print "celebrityLists == " + celebrityLists
print "ids == " + idLists
try:
    l = StdOutListener()
    stream = tweepy.Stream(auth, l)
    stream.filter(follow=[idLists])#,filter_level='low'
except:
    pass
