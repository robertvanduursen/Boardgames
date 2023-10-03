import re
from multiprocessing.pool import ThreadPool as Pool
import requests
import urllib.request

import urllib3
import html2text
import re,os,sys
from text_functions import *

'''
-----------------------------------------------
FIRST EFFORT TO A NEURAL NETWORK KIND OF APPROACH

'''

# parse a folder's files
path = 'C:/Users/Robert/Desktop/wiki_thrawler/Bloodborne/info/'
sys.path.append(path)

# check the directory for files with functions
modules = []
sub = []
for path, subdirs, files in os.walk(path):
        #print (path)
        #print (files)
        for filepath in files:
        	modules.append(path +'/'+ filepath)

fullDict = {}
namesList = []
textDump = []
# parse all the files
for readPath in modules:

	# this will replace the fullDict for the local scope of the current file
	fileItems = []

	ins = open(readPath, "r" )
	#print (readPath)
	textFound = False
	dialogueFound = False
	skip = False

	# Read the file
	# collect all words, line and texts eligable for parsing
	# reformat / un-linebreak / clean-up
	# analyse afterwards

	# also parse the file name itself
	filename = readPath.split("/")[-1].split(".")[0].lower()
	filename = filename.replace("(","").replace(")","")
	fileItems.append(filename.lstrip()+'#')

	for line in ins.readlines():
		if 'text>' in line:
			# applies to characters and enemies
			textFound = True
			line = line[5:]
		if 'title>' in line:
			# applies to characters and enemies
			textFound = True
			line = line[6:]
		if 'dialogue>' in line:
			textFound = False
			dialogueFound = True
			line = line[9:]
		if 'info/upgrade' in readPath or 'info/armor' in readPath or 'info/firearms' in readPath or 'info/chalices' in readPath or 'info/items' in readPath or 'info/shields' in readPath or 'info/weapons' in readPath:
			textFound = True
		#if 'info/bosses' in readPath:
		#	textFound = True

		line = re.sub(r'[\\]',r'',line)

		# parse all 'regular' text found; just plain lines / text
		if textFound and line.isspace() == False and line != '\n' and len(line) > 0:
			if len(line) > 0:
				fileItems.append(line)

		# ------------------------------------------------------
		# parse the dialogue just for words
		if dialogueFound == True and line.isspace() == False and line != '\n' and len(line) > 0:
			# check if line is not multiple sentences#
			if '<' in line:
				skip = True
			else:
				skip = False
			if skip == False:
				fileItems.append(line)


	ins.close()

	# now start analysing
	textDump.append(fileItems)

	for item in fileItems:
		item = re.sub(r'[\n|\\]',r'',item)

		# if there is a space in item, presume multiple words
		if ' ' in item:
			words = item.split(' ')
		else:
			words = item

		for word in words:
			if word not in fullDict.keys():
				fullDict[word] = 1
			else:
				# increase frequency
				fullDict[word] = fullDict[word] + 1

wordCount = 0
for x in fullDict.values():
	wordCount += x
print(wordCount)

#---------------------------------
fullText = sorted(list(set(fullDict.keys()))) # sorted alphabetically

# add to unique word list - every word!!
writePath = "C:/Users/Robert/Desktop/wiki_thrawler/Bloodborne/files/new/fullList.txt"
ins = open(writePath, "w" )
for word in fullText:
		ins.write(word + '\n')
ins.close()
#---------------------------------

# add to freq list
writePath = "C:/Users/Robert/Desktop/wiki_thrawler/Bloodborne/files/new/textdump.txt"
ins = open(writePath, "w" )
for word in textDump:
		toWrite = '%'.join(word).replace('\n','')
		#toWrite = re.sub(r'[\n|\\]',r'',str(word))
		ins.write(toWrite + '\n')
ins.close()

files = []
fileNr = -1
readPath = "C:/Users/Robert/Desktop/wiki_thrawler/Bloodborne/files/new/textdump.txt"
ins = open(readPath, "r" )
for line in ins.readlines():
	if '#' in line:
		fileNr += 1
		files.append('')
	files[fileNr] += line
ins.close()

infoDict = {}
# word as key; values = frequency,isItCapitalized,surroundPunc,wordsFoundOnTheLeft,wordsFoundOnTheright
for item in files:
	splitted = item.split('#')
	name = splitted[0]
	text = ' '.join(splitted[1:])
	text = text.replace('%','')

	name = name.split(' ')
	for word in name:
		word = word.toupper()
		if len(name) > 1:




'''
writePath = "C:/Users/Robert/Desktop/wiki_thrawler/Bloodborne/files/new/textdump.txt"
ins = open(writePath, "w" )
for word in textDump:
		ins.write('#')
		toWrite = '%'.join(word).replace('\n','')
		#toWrite = re.sub(r'[\n|\\]',r'',str(word))
		ins.write(toWrite + '\n')
ins.close()
'''

#----------------
print ("FINISHED")