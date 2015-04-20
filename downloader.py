#! python

# python 2.*, not python 3


# this is a downloader script for downloading files from bbcpoker.bplaced.net/exp3/bbcbot to botfiles/
# it is efficient: it only downloads when the file has changed

# TODO: decide if this script should run always or just be called every 5 minutes

import hashlib
import urllib2
import os.path


def makeemptyfile(fname):
	if os.path.exists(fname): return
	f=open(fname,"w")
	f.write("")
	f.close()
	return

def downloadfile(url,local):
	print "downloading file "+url+"..."
	response = urllib2.urlopen(url)
	file1=open(local,"w")
	file1.write(response.read())
	file1.close()
	print "...done"
	return

def checkhash2():
	response = urllib2.urlopen('http://bbcpoker.bplaced.net/exp3/bbcbot/hash2.txt')
	data1 = response.read()
	data2=data1.split("\n")
	# data3=[x.split(" ",2)[0] for x in data2]
	# data4=[x.split(" ",2)[1] for x in data2]
	makeemptyfile('botfiles/hash2.txt')
	file5=open("botfiles/hash2.txt","r")
	data5=file5.read()
	file5.close()
	data6=data5.split("\n") 
	data7=[x.split(" ",2)[0] for x in data6 if x!=""]
	data8=[x.split(" ",2)[1] for x in data6 if x!=""]
	data9=[]
	# start comparing files
	for row in data2:
		newhash=row.split(" ",2)[0]
		filename1=row.split(" ",2)[1]
		isnew=True
		if filename1 in data8:
			pos=data8.index(filename1)
			if data7[pos]==newhash: isnew=False
		if isnew:
			downloadfile('http://bbcpoker.bplaced.net/exp3/bbcbot/'+filename1,"botfiles/"+filename1)
			makeemptyfile('botfiles/'+filename1)
			newhas=hashlib.md5(open('botfiles/'+filename1, 'r').read()).hexdigest()
		data9.append(newhash+" "+filename1)
	dataA="\n".join(data9)
	file5=open("botfiles/hash2.txt","w")
	file5.write(dataA)
	file5.close()
	newhash1=hashlib.md5(open('botfiles/hash2.txt', 'r').read()).hexdigest()
	file5=open("botfiles/hash1.txt","w")
	file5.write(newhash1)
	file5.close()
	return

def checkhash1():
	# check if folder exists, otherwise create
	if not os.path.isdir('botfiles'): 
		os.makedirs('botfiles')
	response = urllib2.urlopen('http://bbcpoker.bplaced.net/exp3/bbcbot/hash1.php')
	webhash = response.read()
	makeemptyfile('botfiles/hash1.txt')
	hash1file=open("botfiles/hash1.txt","r")
	hash1=hash1file.read()
	hash1file.close()
	if hash1!=webhash : checkhash2()
	return

try:
	print "[python] welcome to the downloader script"
	checkhash1()
	print "[python] Done."
except:
	print "[python] Sorry, there was an error in the downloader"
	# TODO: ...
	exit(1)

