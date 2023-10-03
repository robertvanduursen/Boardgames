
url = r"https://www.playgwent.com/en/decks/3fedd07aa87077eec60f20b539019ad6"

validDecks = [
    ('https://www.playgwent.com/en/decks/a39ea683f67392a3cddc8ae2058d632a', "get me my keys", "scoia"),

    ('https://www.playgwent.com/en/decks/673d42629c6cedb4d32fe950921aa941', "elfy delphi", "scoia"),

    ('https://www.playgwent.com/en/decks/9a8e7115bb8fdcf398e16ae32d481728', "modded NR", "northern realms"),

    ('https://www.playgwent.com/en/decks/534e7d017938f2652a3f2d14ebead4a9', "monster starter deck", "monsters"),

    ('https://www.playgwent.com/en/decks/1e02bea185b2800726b619cace35c768', "smell the blood", "monsters"),

    ('https://www.playgwent.com/en/decks/de27e5a39202d26bc2b0fed1aa3b8b70', "socia starter", "scoia"),

    ('https://www.playgwent.com/en/decks/1ef5d7a772552c93e18d4dd829b1e3c4', "max cards scoai test - guerilla tacticsd", "scoia"),

    ('https://www.playgwent.com/en/decks/7c9be180a5354e160bd87d456b5793da', "max cards scoai test - guerilla tacticsd", "scoia"),

#cant share invalid decks

]

for deck in validDecks:
    url = deck[0]

    code = url.split('/')[-1]


    print(deck[1], code)

    incr = 1

    print(len(code)/incr)
    intString = []
    for x in range(0, 32, incr):
        bit = code[x:x+incr]
        hexa = "0x%s" % bit
        intString.append(eval(hexa))

    print(intString)
    print()

    # for x in range(0,32,incr):
    #     bit = code[x:x+incr]
    #     hexa = "0x%s" % bit
    #     print(hexa, '->', eval(hexa))


'''

URL is just a random key in their database?

no easy commonalities?

changing byte chunks from 1,2,4,8 chars doesnt show any pattern

'''

def offline():
    """ the offline temp data storage for Gwent """
    # C:\Users\rober\AppData\LocalLow\CDProjektRED\Gwent\RemoteAssets\Assets
    #C:\Users\rober\AppData\Local\Temp\CDProjektRED\Gwent

