"""

utlity functions for processing source data to custom format for
Gwent: Iron Judgement

"""


import json, re, sys, os



root = r'C:\Users\rober\Google Drive\Games\Gwent\source'
target = r'C:\Users\rober\Google Drive\Games\Gwent\data'


def sourceToData():
    # remove extranious data
    cards = json.load(open(root + '\cards.json'))
    for name,card in cards.items():
        card['info'] = card['info']['en-US']
        card['name'] = card['name']['en-US']
        card['flavor'] = card['flavor']['en-US']
        card['infoRaw'] = card['infoRaw']['en-US']
        # for tag in set(card['info'].keys()) - {'en-US'}:
        #     #print(card['info']['en-US'])
        #     del card['info'][tag]
    with open(target + '\cards.json','w') as savefile:
        json.dump(cards, savefile)


    ### categories
    cats = json.load(open(root + '\categories.json'))
    for cat, catData in cats.items():
        cats[cat] = catData['en-US']
    with open(target + '\categories.json','w') as savefile:
        json.dump(cats, savefile)


    ### keywords
    keywords = json.load(open(root + '\keywords.json'))
    for word,card in keywords.items():
        keywords[word] = card['en-US']['text']
    with open(target + '\keywords.json','w') as savefile:
        json.dump(keywords, savefile)

sourceToData()


def validataData():
    cards = json.load(open(target + '\cards.json'))
    for name,card in cards.items():
        print(card['name'])
        print(card['info'])
        print(card['flavor'])
        print(card['infoRaw'])

# validataData()
