import tweepy 


consumer_key = "YDziQrusHVhKLSEPsAwjwPnBM"
consumer_secret = "aKqikjWYIYwGX2gfntTNNdu045Qgm6e5t8TsJ11YOv04IL9G4U"
access_key = "1342875894893793281-LbHOVSOKvxcqYbS744o4YI2A8hPyXC"
access_secret = "YmlR1rLjvdMZU4rflmK3vwTK4AUVSL00Vcdfzp27zSsAv"

# Function to extract tweets 
def get_tweets(username):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username, 
                           # 200 is the maximum allowed count
                           count=10,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    
    for info in tweets[0:10]:
    
     print("ID: {}".format(info.id))
     print(username)
     print(info.created_at)
     print(info.full_text)


if __name__ == '__main__': 
	get_tweets('@CBSDSchools')
