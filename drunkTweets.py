# drunktweet.py
# http://dabeaz.blogspot.com/
'''
Print out possible drunk tweets from the city of Chicago.
'''

import regex
import requests
import json

# Terms for being "wasted"
terms = { 'drunk','wasted','buzzed','hammered','plastered' }

# A fuzzy regex for people who can't type
pat = regex.compile(r"(?:\L<terms>){i,d,s,e<=2}$", regex.I, terms=terms)

# Connect to the Twitter streaming API
url   = "https://stream.twitter.com/1/statuses/filter.json"
parms = {
    'locations' : "-87.94,41.644,-87.523,42.023"    # Chicago
    }
auth  = ('username','password')
r = requests.post(url, data=parms, auth=auth)

# Print possible candidates
for line in r.iter_lines():
    if line:
        tweet = json.loads(line)
        status = tweet.get('text',u'')
        words = status.split()
        if any(pat.match(word) for word in words):
           print(tweet['user']['screen_name'], status)