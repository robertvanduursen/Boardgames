import re
from multiprocessing.pool import ThreadPool as Pool
#import requests
#import urllib.request

#import urllib3
#import html2text
import re,os,sys
#from text_functions import *

localPath = 'C:/Users/gbduursr/Desktop/self/'
puncts = [',','.',':','\'','"','!','?',';']

def singleSpace(text):

	return text

def hasPunc(text):
	result = False
	for x in puncts:
		if x in text:
			result = True
	return result

def stripPunc(text):
	newText = text
	for x in puncts:
		newText = newText.replace(x,'')
	return newText

'''
-----------------------------------------------
FIRST EFFORT TO A NEURAL NETWORK KIND OF APPROACH

'''
class Word(object):
	# frequency,isItCapitalized,surroundPunc,wordsFoundOnTheLeft,wordsFoundOnTheright
    __slots__ = ['name', 'frequency','canCapital','onlyCapital','wordsLeft','wordsRight','surroundPunc','startWord','wordPuncts','puncFreq','onlyFirst','length','capNotFirst','simWords']
    def __init__(self, name):
        self.name = name.title()
        self.frequency = 0
        self.startWord = False
        self.canCapital = False
        self.onlyCapital = True
        self.capNotFirst = False
        self.surroundPunc = False
        self.onlyFirst = True
        self.puncFreq = 0
        self.length = 0
        self.wordPuncts = []
        self.wordsLeft = []
        self.wordsRight = []
        self.simWords = []

    def updateName(self,newName):
    	pass

    def updateFreq(self,freq):
    	self.frequency += freq

    def updatePuncFreq(self,freq):
    	self.puncFreq += freq

    def setStart(self,state):
    	self.startWord = state 

    def setLength(self,leng):
    	self.length = leng 

    def setCapital(self,state):
    	self.canCapital = state

    def setCapNotFirst(self,state):
    	self.capNotFirst = state

    def changeCapital(self,state):
    	self.onlyCapital = state
    	self.name = self.name.lower()

    def setPunc(self,state):
    	self.surroundPunc = state

    def setOnlyFirst(self,state):
    	self.onlyFirst = state 

    def addWordLeft(self,word):
    	self.wordsLeft.append(word)

    def addWordRight(self,word):
    	self.wordsRight.append(word)

    def addWordPuncts(self,pnct):
    	if pnct not in self.wordPuncts:
    		self.wordPuncts.append(pnct)

    def addSimWord(self,wrd):
    	if wrd not in self.simWords:
    		self.simWords.append(wrd)

files = []
fileNr = -1
readPath = localPath + "textdump.txt"
ins = open(readPath, "r" )
for line in ins.readlines():
	if '#' in line:
		fileNr += 1
		files.append('')
	files[fileNr] += line
ins.close()

infoDict = {}
lineRecord = []
# word as key; values = frequency,isItCapitalized,surroundPunc,wordsFoundOnTheLeft,wordsFoundOnTheright
for item in files:
	splitted = item.split('#')
	name = splitted[0]
	text = ' '.join(splitted[1:])
	text = text.replace('\n','')
	text = text.replace('%',' ')


	name = name.split(' ')
	incr = 0
	for word in name:
		if word.lower() not in infoDict.keys():
			infoDict[word.lower()] = Word(word.lower())
			infoDict[word.lower()].setLength(len(word))
		if word.lower() in infoDict.keys():
			wordClass = infoDict[word.lower()]
			wordClass.updateFreq(1)

			if word.istitle():
				wordClass.setCapital(True)
			else:
				wordClass.changeCapital(False)
			if len(word) > 1 and incr == 0:
				wordClass.setStart(True)
			if len(name) > 1:
				if incr != 0:
					# try left
					wordClass.addWordLeft(name[incr-1])
				if incr != len(name)-1:
					# try right
					wordClass.addWordRight(name[incr+1])
		incr += 1

	# Madatory left and right strip due to % and #
	text = singleSpace(text.lstrip().rstrip())
	#if 'Doubtless' in text:
	#	print (text)

	parseText = text.split('.')


	for sentence in parseText:
		incr = 0
		lineRecord.append(sentence.lstrip().rstrip())
		sentence = (sentence.lstrip().rstrip()).split(' ')
		for word in sentence:
			if len(word) > 0:
				parseWord = word

				if hasPunc(word):
					parseWord = stripPunc(word)

				if parseWord.lower() not in infoDict.keys():
					infoDict[parseWord.lower()] = Word(parseWord.lower())
					infoDict[parseWord.lower()].setLength(len(parseWord))
				if parseWord.lower() in infoDict.keys():
					wordClass = infoDict[parseWord.lower()]
					wordClass.updateFreq(1)

					if word.istitle():
						wordClass.setCapital(True)
					else:
						wordClass.changeCapital(False)
					if len(word) > 1 and word[-1] in puncts and word[-1] != '.':
						wordClass.setPunc(True)
						wordClass.addWordPuncts(word[-1])
						wordClass.updatePuncFreq(1)
					if len(word) > 1 and incr == 0:
						wordClass.setStart(True)
					if len(word) > 1 and incr != 0:
						wordClass.setOnlyFirst(False)
						if word.istitle():
							wordClass.setCapNotFirst(True)

					if len(sentence) > 1:
						if incr != 0:
							# try left
							leftword = sentence[incr-1]

							# carefull, this may also mean that this word is the first word in a sentence
							if hasPunc(leftword):
								if '.' in leftword or '?' in leftword or '!' in leftword:
									wordClass.setStart(True)
								leftword = stripPunc(leftword)
							if leftword != '':
								wordClass.addWordLeft(leftword)
						if incr != len(sentence)-1:
							# try right
							rightword = sentence[incr+1]
							if hasPunc(rightword):
								rightword = stripPunc(rightword)
							if rightword != '':
								wordClass.addWordRight(rightword)
			incr += 1


'''
query = "willem".lower()
print(infoDict[query])
print('name: ' + infoDict[query].name)
print('frequency: ' + str(infoDict[query].frequency))
print('canBeCapital: ' + str(infoDict[query].canCapital))
print('onlyCapital: ' + str(infoDict[query].onlyCapital))
print('capNotFirst: ' + str(infoDict[query].capNotFirst))
print('length: ' + str(infoDict[query].length))
print('startWord: ' + str(infoDict[query].startWord))
print('onlyFirst: ' + str(infoDict[query].onlyFirst))
print('surroundPunc: ' + str(infoDict[query].surroundPunc))
print('puncFreq: ' + str(infoDict[query].puncFreq))
print(infoDict[query].wordPuncts)
print(infoDict[query].wordsLeft)
print(infoDict[query].wordsRight)
'''

freqDict = {}
for word in infoDict.keys():
	wordclass = infoDict[word]

	# freq, start, mid, end, capBool
	incr = 0
	for letter in wordclass.name.lower():
		if letter not in list(freqDict.keys()):
			freqDict[letter] = [1,0,0,0,0]
		if letter in list(freqDict.keys()):
			freqDict[letter][0] += 1
			if letter.isupper():
				freqDict[letter][4] = 1
			if incr == 0:
				freqDict[letter][1] += 1
			if incr == len(wordclass.name)-1:
				freqDict[letter][3] += 1
			if incr != 0 and incr != len(wordclass.name)-1:
				freqDict[letter][2] += 1
		incr += 1
'''
for plz in sorted(freqDict.items(), key=lambda lol: (-lol[1][1], lol[0])):
	if plz[1]:
		print(plz[0] + ' ' + str(plz[1][1]))
'''

'''
# WARNING: LONG OPERATION
print ("START")
langDict = {}
for item in infoDict.keys():
	wordName = infoDict[item]
	incr = 0
	word = wordName.name.lower()
	
	for x in range(2,len(word)):
		attempt = word[0:x]
		if attempt not in list(langDict.keys()):
			langDict[attempt] = 1
		if attempt in list(langDict.keys()):
			langDict[attempt] += 1
	
	for x in range(len(word)-2,0,-1):
		attempt = word[x:len(word)]
		if attempt not in list(langDict.keys()):
			langDict[attempt] = 1
		if attempt in list(langDict.keys()):
			langDict[attempt] += 1


print (len(langDict.keys()))
for plz in sorted(langDict.items(), key=lambda lol: (-lol[1], lol[0])):
	if plz[1] > 9:
		print(plz[0] + ' ' + str(plz[1]))


for plz in sorted(infoDict.items(), key=lambda lol: (-lol[1].length, lol[0])):
	#if plz[1].onlyCapital:
	print(plz[1].name + ' ' + str(plz[1].frequency))


'''
'''
for plz in sorted(infoDict.items(), key=lambda lol: (-lol[1].frequency, lol[0])):
	#if plz[1].onlyCapital:
	print(plz[1].name + ' ' + str(plz[1].frequency))
'''

# ATTEMPT at word similarity
def similar(word1,word2):
	# how similar is word1 to word2. i.e. 'link' to 'linked' ipv 'line'
	if len(word1) == len(word2):
		longword = word1
		shortword = word2
	else:
		if len(word1) > len(word2):
			longword = word1
			shortword = word2
		else:
			longword = word2
			shortword = word1

	# if shortword is fully included in longword: return 10
	# if longword starts or ends with shortword: return 9
	# if it isnt included or has nothing: return 0
	incr = 0
	if shortword in longword:
		incr = 10
		#if longword.endswith(shortword):
		#	pass
	
	'''
	for x in range(len(shortword)):
		if longword[x] == shortword[x]:
			incr += 1
		else:
			incr = 0
			break
	'''
	return incr


print ("similarity")
# test similarity based on having similar strings, refine bad results later based on other conditions
langDict = {}
simList = list(infoDict.keys())
for item in infoDict.keys():
	wordClass = infoDict[item]
	localList = list(set(simList) - set(list(wordClass.name)))

	incr = 0
	for test in localList:
		if test != '':
			simTest = similar(wordClass.name,test)
			if simTest > 8:
				wordClass.addSimWord(test)


print ("GO")

# SAVE THE WORDS!!
writePath = localPath + "wordDump.py"
ins = open(writePath, "w" )
ins.write('wordDict = {\n')

incr = 0
tot = len(infoDict.keys())
for item in sorted(infoDict.keys()):
	wordClass = infoDict[item]
	ins.write('[')
	ins.write(str(wordClass.name)+',')
	ins.write(str(wordClass.frequency)+',')
	#ins.write(str(wordClass.canCapital)+',')
	#ins.write(str(wordClass.capNotFirst)+',')
	#ins.write(str(wordClass.length)+',')
	#ins.write(str(wordClass.startWord)+',')
	#ins.write(str(wordClass.onlyFirst)+',')
	#ins.write(str(wordClass.surroundPunc)+',')
	#ins.write(str(wordClass.puncFreq)+',')
	#ins.write(str(wordClass.wordPuncts)+',')
	#ins.write(str(wordClass.wordsLeft)+',')
	#ins.write(str(wordClass.wordsRight)+',')
	ins.write(str(wordClass.simWords))

	if incr != tot-1:
		ins.write('],\n')
	else:
		ins.write(']\n')
	incr += 1

ins.write('}')
ins.close()


writePath = localPath + "sentenceBinary.py"
ins = open(writePath, "w" )

vowels = ['o','e','a','u','i','y']
for record in lineRecord:
	converted = ''
	for char in record:
		if char == ' ':
			converted += '_'
		elif char in vowels:
			converted += '0' 
		else:
			converted += '1' 

	ins.write(converted + '\n')


ins.close()
#----------------
print ("FINISHED")