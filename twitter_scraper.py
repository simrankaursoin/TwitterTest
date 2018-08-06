from twitterscraper import query_tweets

all_tweets = []
all_users = []
all_times = []
document = open("data6.txt", "w+")
for tweet in query_tweets("PyCon", 4):
    all_tweets.append(tweet.text)
    all_users.append(tweet.user)
    all_times.append(tweet.timestamp)
document.write(" TWEETS : \r\n")
for i in all_tweets:
    document.write(i + "\r\n \r\n")
document.write("\r\n \r\nUSERS : \r\n")
for i in all_users:
    document.write(i + "\r\n \r\n")
document.write("\r\n \r\nTIMESTAMPS : \r\n")
for i in all_times:
    document.write(str(i) + "\r\n \r\n")
