import webbrowser
from requests_oauthlib import OAuth1Session

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'


def get_access_token(consumer_key, consumer_secret):

    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret)

    url = oauth_client.authorization_url(AUTHORIZATION_URL)

    webbrowser.open(url)
    pincode = raw_input('Pincode? ')

    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
            resource_owner_key=resp.get('oauth_token'),
            resource_owner_secret=resp.get('oauth_token_secret'),
            verifier=pincode
            )
   
    print 'Your Twitter Access Token key: %s' % resp.get('oauth_token')
    print 'Access Token secret: %s' % resp.get('oauth_token_secret')


def main():
    consumer_key = raw_input('Enter your consumer key: ')
    consumer_secret = raw_input("Enter your consumer secret: ")
    get_access_token(consumer_key, consumer_secret)

if __name__ == "__main__":
    main()
