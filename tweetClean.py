# python program to help clean up tweets
# file loads, data cleans, and words counted

data = open('TweetBackup15June2012').read().lower()

data = data.replace('''http://t.co/''',' ')
data = data.replace('''\n''',' ')
data = data.replace('''+0000''',' ')
data = data.replace('''!''',' ')
data = data.replace('''$''',' ')
data = data.replace('''%''',' ')
data = data.replace('''^''',' ')
data = data.replace('''&''',' ')
data = data.replace('''*''',' ')
data = data.replace(''':''',' ')
data = data.replace(''';''',' ')
data = data.replace('''<''',' ')
data = data.replace('''>''',' ')
data = data.replace('''{''',' ')
data = data.replace('''}''',' ')
data = data.replace('''[''',' ')
data = data.replace(''']''',' ')
data = data.replace('''|''',' ')
data = data.replace('''-''',' ')
data = data.replace('''+''',' ')
data = data.replace('''=''',' ')
data = data.replace(''' rt ''',' ')
data = data.replace(''' 2011 ''',' ')
data = data.replace(''' 2012 ''',' ')
data = data.replace(''' mon ''',' ')
data = data.replace(''' tue ''',' ')
data = data.replace(''' wed ''',' ')
data = data.replace(''' thu ''',' ')
data = data.replace(''' fri ''',' ')
data = data.replace(''' sat ''',' ')
data = data.replace(''' sun ''',' ')
data = data.replace(''' jan ''',' ')
data = data.replace(''' feb ''',' ')
data = data.replace(''' mar ''',' ')
data = data.replace(''' apr ''',' ')
data = data.replace(''' may ''',' ')
data = data.replace(''' jun ''',' ')
data = data.replace(''' jul ''',' ')
data = data.replace(''' aug ''',' ')
data = data.replace(''' sep ''',' ')
data = data.replace(''' oct ''',' ')
data = data.replace(''' nov ''',' ')
data = data.replace(''' dec ''',' ')
data = data.replace('''\x9c''',' ')
data = data.replace('''\xe2''',' ')
data = data.replace('''\xa2''',' ')
data = data.replace('''\xe3''',' ')
data = data.replace('''/''',' ')
data = data.replace('''~''',' ')
data = data.replace(''' the ''',' ')
data = data.replace(''' to ''',' ')
data = data.replace(''' and ''',' ')
data = data.replace(''' is ''',' ')
data = data.replace(''' on ''',' ')
data = data.replace(''' for ''',' ')
data = data.replace(''' a ''',' ')
data = data.replace(''' in ''',' ')
data = data.replace('''...''',' ')
data = data.replace(''' with ''',' ')
data = data.replace(''' it ''',' ')
data = data.replace(''' that ''',' ')
data = data.replace(''' are ''',' ')
data = data.replace(''' https''',' ')

data = data.replace(''' i ''',' ')
data = data.replace(''' of ''',' ')
data = data.replace(''' my ''',' ')
data = data.replace(''' at ''',' ')
data = data.replace(''' what ''',' ')
data = data.replace(""" i'm""",' ')
countList={}
sortedCountList={}
data = data.split()
for word in data:
	if word in countList :
		countList[word] = countList[word]+1
	else :
		countList[word] = 1

inverse = [(value, key) for key, value in countList.items()]
sortedCountList = sorted(inverse)

outdata = ' '.join(countList)
fh = open('test','w')
fh.write(outdata)
fh.close()