#! /usr/bin/python

'''
Python program to rip Follower ID's of a targetTwitterUser
Note small difference in API call to followers *** NOT FRIENDS ***
version 0.1 alpha @dgleebits
'''

import sys
import time
import os
import tweepy

CONSUMER_KEY = 'ASDFASDFASDF'
CONSUMER_SECRET = 'ASDFSDFASDFSADF'

ACCESS_KEY = 'ASDFASDFSDF'
ACCESS_SECRET = 'ASDFASDFSDFSDFASDF'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


#dependency is the tweepy package download at: http://code.google.com/p/tweepy/
#global
pathToFile = sys.argv[1]

f = open(pathToFile, 'r')
for targetTwitterUser2 in f.readlines():
  print "working on " + targetTwitterUser2
  followers2ndLevel = tweepy.api.followers_ids(targetTwitterUser2)

  f = open('2ndLevelDump_'+targetTwitterUser2, 'w')
  for follower in followers2ndLevel:
    output = follower
    print follower
    f.write("%s\n" % follower)
  f.close()

f.close()