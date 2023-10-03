import urllib.request,sys,os
import operator,os,re,sys,inspect # default imports
import sqlite3

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(currentPath)

url = r'https://keyforge-compendium.com'

def createCardTable():
	conn = sqlite3.connect("cards.db")
	conn.execute('''CREATE TABLE cards (
	Name text,
	CardText text,
	TypeAction text, 
	House text, 
	Aember text, 
	Power real,
	Armor  real,
	Rarity  text,
	Artist  text,
	FlavorText text,
	Number real,
	Sets text,
	InDecks text,
	ADHD text)''')
	conn.commit()


def getCards(url):
	result = False
	try:
		f = urllib.request.urlopen(url)
		result = f.read()
		print('done')
	except:
		print('scraping didnt work for some reason')

	return result


class Card:
	Name = False
	CardText = False
	TypeAction = False
	House  = False
	Aember  = 0
	Power  = 0
	Armor  = 0
	rarity  = False
	Artist  = False
	FlavorText  = False
	Number  = 0
	Sets  = False
	InDecks  = False
	ADHD  = False

	def __init__(self):
		pass

def getCard(url,card):
	result = False
	url = url + '/sets/' + card

	try:
		f = urllib.request.urlopen(url)
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
		print('done w {}'.format(card))
	except:
		print('getting card didnt work for some reason')
	if result:
		text = str(result)
		newCard = Card()

		match = re.search(r"<title>(.*?) Keyforge Compendium</title>", text)
		newCard.Name = match.groups()[0][:-1].strip() if match is not None else 'no name'

		newCard.CardText = re.search(r"<strong>Card Text</strong>(.*?)</li>", text).groups()[0].replace('"','\'')
		newCard.TypeAction = re.search(r"<strong>Type</strong>(.*?)</li>", text).groups()[0].strip()

		match = re.search(r"<strong>House</strong>(.*?)</li>", text)
		newCard.House = match.groups()[0].strip() if match is not None else ''

		match = re.search(r"<strong>\\xc3\\x86mber</strong>(.*?)</li>", text)
		newCard.Aember = match.groups()[0] if match is not None else 0

		match = re.search(r"<strong>Power</strong>(.*?)</li>", text)
		newCard.Power = match.groups()[0] if match is not None else 0

		match = re.search(r"<strong>Armor</strong>(.*?)</li>", text)
		newCard.Armor = match.groups()[0] if match is not None else 0

		newCard.rarity = re.search(r"<strong>Rarity</strong>.*?/>(.*?)</li>", text).groups()[0]
		newCard.Artist = re.search(r"<strong>Artist</strong>(.*?)</li>", text).groups()[0]

		match = re.search(r"<strong>Flavor text</strong>(.*?)</li>", text)
		newCard.FlavorText = match.groups()[0] if match is not None else ''

		newCard.Number = re.search(r"<strong>Number</strong>(.*?)</li>", text).groups()[0]
		newCard.Sets = re.search(r"<strong>Set</strong>(.*?)</li>", text).groups()[0]
		newCard.InDecks = re.search(r"<strong>In Decks</strong>(.*?)</li>", text).groups()[0]
		newCard.ADHD = re.search(r"<strong>ADHD</strong>(.*?)</li>", text).groups()[0]

		return newCard
	else:
		print(url,'returned empty?')
		return False


conn = sqlite3.connect("cards.db")

# card = getCard(url,'1-cota/cards/1-anger')
# conn.execute("INSERT OR REPLACE INTO cards VALUES ('%s','%s','%s', '%s' ,%s ,%s ,%s ,'%s','%s','%s',%s,'%s','%s','%s')" % (
# 	card.Name, card.CardText, card.TypeAction, card.House, card.Power, card.Armor, card.Aember, card.rarity,
# 	card.Artist, card.FlavorText, card.Number, card.Sets, card.InDecks, card.ADHD ))

cardString = getCards(url)
cardsFound = re.findall(r'<a href="/sets/(.*?)">',str(cardString))
print(len(cardsFound))
for x in cardsFound:
	card = getCard(url, x)
	if card:
		comm = '''INSERT OR REPLACE INTO cards VALUES ("%s", "%s", "%s", "%s", %s, %s, "%s", "%s", "%s", "%s", %s, "%s", "%s", "%s")''' % (
			card.Name, card.CardText, card.TypeAction, card.House, card.Aember, card.Power, card.Armor,  card.rarity,
			card.Artist, card.FlavorText, card.Number, card.Sets, card.InDecks, card.ADHD)
		try:
			conn.execute(comm)
			print(card.Number, card.Name, '= added')
		except Exception as err:
			print(card.Name, '-> didnt work:',err)
			print(card.Number, '-> maybe this helps')
			print(comm)
			for attr in card.__dict__.items(): print(attr)
			break
conn.commit()

