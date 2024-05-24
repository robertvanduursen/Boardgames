'''
14
16
11
10
8
9
'''


"""

Bard

Cleric

    Druid

Fighter

    Monk

Paladin  lvl 1 tot 2
https://5e.tools/classes.html#paladin_phb,state:ishidefeatures=b1~isshowfluff=b1
https://5e.tools/races.html#dwarf%20(hill)_phb
https://5e.tools/book.html#phb,1,1.%20choose%20a%20race

Ranger

    Rogue

Sorcerer

    Warlock

Wizard


Wat is je persoonlijke missie in de Underdark


https://5e.tools/charcreationoptions.html#anvilwrought_mot
https://5e.tools/lifegen.html
https://5e.tools/items.html#holy%20symbol_phb
https://5e.tools/items.html#spear_phb
https://5e.tools/backgrounds.html#guild%20artisan_phb
https://5e.tools/languages.html#abyssal_phb
https://5e.tools/items.html#smith's%20tools_phb
https://5e.tools/items.html#traveler's%20clothes_phb
https://5e.tools/items.html#tinker's%20tools_phb
https://5e.tools/classes.html#artificer_tce
https://5e.tools/races.html#dwarf%20(hill)_phb

https://roll20.net/

https://i.imgur.com/T0b3exW.png


https://5e.tools/classes.html#paladin_phb,state:isshowfluff=b1~sub-watchers-tce=b1

"""

def todo():
    '''
    I like to talk at length about my profession.

    Wie

    Wat

    Waar

    Hoe zijn we hier gekomen/Waarom zijn ze naar de Underdark gegaan?


    Introductie Scene
    Hoe is de partij bij jou gekomen?


    :return:
    '''
    pass

'''
BACKSTORY
    Torek Goldbeard

    Once called Ironbeard, I was a humble smith and brewmaster before I joined the ranks of the Paladins.
    Amongst the Cast, there is a woman so beautiful and fierce with a hammer that she ushered a Trail By Anvil for her affection
    The trial was mighty, but when the metal cooled I had found my better.
    I lost that day; but my fair lady did not choose the winner cos he was too proud.


    I searched high and low for a means to prove my worthiness and win her favour. In my search in the Guild halls, I stumbled upon a text most strange.
    It somehow spoke to me, but I did not understand it. The forgemaster bade me to ask the Paladins.

    When I asked the head of the Order of the Hammer and the Shield, his normal jolly humour turned serious in an instant.
    "Why do you seek this my lad?", he said I answered. He sighed: "I fear there is nothing to sway you from the path you are about to embark on."
    "Very well then, you seek a metal of the gods. Our legends speak of a source that resides in the Underdark."
    "What you may find there only the gods know, but it needs purification of its taint"

    "Drink harty, your training begins tomorrow" he ended. That was 50 years ago. I learned the ways of the Order and became a
    Paladin. My oath I uphold is to protect all against the horrors of the beyond.


    I am here to find the ore I seek, and I seek companions on my journey.



CHAR
    Dwarf (Hill)
    Lawful Good
    Guild Artisan


PERSONALITY TRAITS
    I like to talk at length about my profession.


IDEALS
    Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization.
    Beer Bonds

BONDS
    I pursue favour and skill to secure someone's love.


FLAWS
    I'm horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals.
    I have a tendency to destroy and boost to challenge anyone.

    I am bonded to a demon(?)

CLASS
    Paladin w. Interception
    Oath of the Watchers als lvl 3 Oath

LANGUAGES
    Common, Dwarvish, Abyssal

PROFICIENCIES
    Armor: All armor, shields
    Weapons: Simple weapons, martial weapons
    Tools: Smithing Tools, Tinker Tool
'''

import requests
url = 'https://app.roll20.net/editor/character/10043801/-MXs0GtwrWoBWm-LziBU/true?popout=true'


response = requests.get(url)

print(response)
print(response.content)