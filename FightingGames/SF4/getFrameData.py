import urllib.request,sys,os
import operator,os,re,sys,inspect # default imports
import xml.etree.cElementTree as ET
from Fighters import *

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(currentPath)

def getCharData(character):
	result = False
	url = r'http://wiki.shoryuken.com/Ultra_Street_Fighter_IV/'
	try:
		f = urllib.request.urlopen(url+character)
		result = f.read()
		'''
		result = str(f.read())

		pages = []
		for x in result.split('<a'):
			link = x.split('>')[0].split('href=')[-1][1:-1]
			if '.html' in link and 'class_' in link:
				print(link)
				pages.append(link)
		'''
		print('done with', character)
	except:
		print(character,'didnt work for some reason')

	if result:
		folder = currentPath+'/data/'+character
		if not os.path.exists(folder): os.makedirs(folder)
		with open(folder+'/frameData.html','wb') as F: F.write(result)

#for char in characters.values(): getCharData(char)


