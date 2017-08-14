import sys
import string
import simplejson
from twython import Twython
import datetime

now = datetime.datetime.now()
day = int(now.day)
month = int(now.month)
year = int(now.year)

t = Twython(app_key='APP_KEY',  # REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
            app_secret='APP_SECRET',
            oauth_token='OAUTH_TOKEN',
            oauth_token_secret='OAUTH_TOKEN_SECRET')
