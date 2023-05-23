import tweepy
from datetime import datetime

dir = "/home/pi/scripts/AperoCycloBot/"


#AUTHENTICATION
twitter_auth_cfg_file = open(dir+"twitter_auth.cfg", 'r')
twitter_auth_cfg = twitter_auth_cfg_file.read().split("\n")
twitter_auth_cfg_file.close()

client = tweepy.Client(
    consumer_key=twitter_auth_cfg[0],
    consumer_secret=twitter_auth_cfg[1],
    access_token=twitter_auth_cfg[2],
    access_token_secret=twitter_auth_cfg[3] )

# Read last stored tweet ID from file
lastTweet_txt = open(dir+"lastTweet.txt", 'r')
lastTweet = lastTweet_txt.readline()
lastTweet_txt.close()

# Search for new tweets
results = client.search_recent_tweets('(#CyclAperoParis OR #AperoVéloParis OR #AperoCycleParis OR #AperoCycloParis OR #AperoCycloRueil) -"Filter:replies" -"Filter:Retweet"', since_id=lastTweet, user_auth=True)


if results.data is not None: # If new tweet is found
    # Reweet
    client.retweet(results.data[0].id)
    print(datetime.now().strftime("%d.%m.%Y %H:%M:%S")+" - Newer tweet found: "+str(results.data[0].id)+"\n")

    
    # Write new toot ID to lastToot.txt
    lastTweet_txt = open(dir+"lastTweet.txt", 'w')
    lastTweet_txt.write(str(results.data[0].id))
    lastTweet_txt.close()
else: #
    print((datetime.now().strftime("%d.%m.%Y %H:%M:%S")+" - No new tweet found \n"))    
