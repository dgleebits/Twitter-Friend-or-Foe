data = open('TweetBackup15June2012').read().lower()

data = data.replace('''http://t.co/''',' ')
data = data.replace('''\n''',' ')
data = data.replace('''RT''',' ')
data = data.replace('''2011''',' ')
data = data.replace('''2012''',' ')
data = data.replace('''+0000''',' ')
data = data.replace('''mon''',' ')
data = data.replace('''tue''',' ')
data = data.replace('''wed''',' ')
data = data.replace('''thu''',' ')
data = data.replace('''fri''',' ')
data = data.replace('''sat''',' ')
data = data.replace('''sun''',' ')
data = data.replace('''jan''',' ')
data = data.replace('''feb''',' ')
data = data.replace('''mar''',' ')
data = data.replace('''may''',' ')
data = data.replace('''jun''',' ')
data = data.replace('''jul''',' ')
data = data.replace('''aug''',' ')
data = data.replace('''sep''',' ')
data = data.replace('''oct''',' ')
data = data.replace('''nov''',' ')
data = data.replace('''dec''',' ')