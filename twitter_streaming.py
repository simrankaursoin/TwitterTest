# twitter_streaming.py
from secure import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from twitter import Twitter, OAuth

#connects to the twitter API
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth) 

def collect_tweets(keywords): 
    #create a .txt file
    document = open("data.txt", "w+")
    all_tweets = []    
    all_users = []  
    all_times = [] 
    tweets = twitter.search.tweets(q=" OR ".join(keywords),
                                   result_type='recent', lang='en', count = 1000)
    tweet = tweets["statuses"]
    for i in tweet:
        if "pycon" in i["user"]["screen_name"] and i["text"][:2] != "RT":
            all_tweets.append(i["text"])
            all_users.append(i["user"]["screen_name"])
            all_times.append(i["created_at"])
    '''
    Format document.
    Add all the tweets, usernames, and timestamps to document
    '''
    document.write(" TWEETS : \r\n")
    for i in all_tweets:
        document.write(i + "\r\n \r\n")
    document.write("\r\n \r\nUSERS : \r\n")
    for i in all_users:
        document.write(i + "\r\n \r\n")
    document.write("\r\n \r\nTIMESTAMPS : \r\n")
    for i in all_times:
        document.write(i + "\r\n \r\n")
        
#list of keywords to search through tweets
keywords = ["#pycon2018", "#PyCon", "pycon", "PyCon"]
#call the function to search through tweets and create text file
collect_tweets(keywords)