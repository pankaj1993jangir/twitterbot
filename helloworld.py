import tweepy, time, sys
argfile = str(sys.argv[1])
CONSUMER_KEY = 'ps2AnAA3k5L0TJ5VPRZ4vm4Ct'	#replace this with your consumer key
CONSUMER_SECRET = 'r0v0vncy3xGI6xZXxnn2wmzPL3Jqujkm0VpZ3hvKuD1MCACF3q'		#replace this with your consumer secret key
ACCESS_KEY = 'L0TJ5V...'	#replace this with your access token
ACCESS_SECRET = 'vncy3xGI6...'	#replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open("helloworld.txt",'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every (900 sec or (900/60)=15 minutes)
