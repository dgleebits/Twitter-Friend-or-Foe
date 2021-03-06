#!/usr/bin/python
import twitter,time,simplejson,urllib

def getFollowers(screenName,cursorPos='-1'):
  """ uses twitter REST API to return a dictionary of followers"""
  url="http://api.twitter.com/1/statuses/followers/%s.json?cursor=%s" % (screenName,cursorPos)
  result=simplejson.load(urllib.urlopen(url))
  entries=result['users']
  return entries, result['next_cursor_str']
  
def getFriends(screenName,cursorPos='-1'):
  """ uses twitter REST API to return a dictionary of followers"""
  url="http://api.twitter.com/1/statuses/friends/%s.json?cursor=%s" % (screenName,cursorPos)
  result=simplejson.load(urllib.urlopen(url))
  try:
    entries=result['users']
  except:
    entries=None
  return entries, result['next_cursor_str']  
  
  


def getUserInfo(user):
  """ uses twitter REST API to return a dictionary based on user """
  url = "http://api.twitter.com/1/users/show/%s.json" % (user)
  userinfo=simplejson.load(urllib.urlopen(url))
  return userinfo
  
def updateFile(fileHandle,user):
  """ given the user and a filename, write a few
      fields to the file.  New fields and calculations can be added to the file
      as necessary"""
  name = user['screen_name']
  tweets = user['statuses_count']
  followers = user['followers_count']
  
  """ as long as the user has >0 follower, determine their
      tweets to followers ratio """
  if followers > 0:
    pct = float(tweets) / float(followers)
  else:
    pct = 0
    
  text="%s\t%s\t%s\t%f" % (name, tweets,followers,pct)
  fileHandle.write(text + '\n')
  
def getAllFollowers(user):
  """ for a given user, return a dict of ALL of their followers"""
  allFollowers={}
  nextCursor = "-1"
  while nextCursor <> "0":
    followers,nextCursor = getFollowers(user,nextCursor)
    for follower in followers:
      allFollowers[follower['screen_name']] = follower
 
  return allFollowers
  
def getAllFriends(user):
  """ for a given user, return a dict of all of their friends"""
  allFriends={}
  nextCursor = "-1"
  while nextCursor <> "0":
    friends,nextCursor = getFriends(user,nextCursor)
    for friend in friends:
      allFriends[friend['screen_name']] = friend 
  return allFriends      
      
def getCelebrityFriends(user):
  """ rough attempt at identifying celebrities.  for the time being
      lets say a celebrity is someone with at least 1M followers
      I need to build a stoplist for users like @cnn, @breakingnews, etc"""
      
  celebrityFriends={}
  threshhold=1000000 
  nextCursor = "-1"
  while nextCursor <> "0":
    friends,nextCursor = getFriends(user,nextCursor)
    for friend in friends:
      if friend['followers_count'] >= threshhold:
        celebrityFriends[friend['screen_name']] = friend
  return celebrityFriends        
        

      
  


def writeFile(uid,type):

  
  file='%s_%s.txt' % (uid,type)
  fileHandle = open(file,'w')
  
  myuser = {}
  myUser = getUserInfo(uid)
  updateFile(fileHandle,myUser)
  

  nextCursor = "-1"
  while nextCursor <> "0": 
    if type=='followers':
      followers,nextCursor = getFollowers(uid,nextCursor)
    else:
      followers,nextCursor = getFriends(uid,nextCursor)
      
    # write to a log

    for ff in followers:
      
      name = ff['screen_name']
      tweets = ff['statuses_count']
      followers = ff['followers_count']
      if followers <> 0:
        pct = float(tweets) / float(followers)
      else:
        pct = 0
        
      text="%s\t%s\t%s\t%f" % (name, tweets,followers,pct)
      fileHandle.write(text + '\n')


  fileHandle.close()
  