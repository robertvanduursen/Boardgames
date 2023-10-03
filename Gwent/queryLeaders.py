
import gwentData, random


leaders = []
for fac in gwentData.Factions.values():
    leaders += fac.Leaders
# faction = gwentGame.Factions['Syndicate']

# can pick cards from 1 faction and Neutral
# combinedFaction = self.faction + gwentGame.Factions['Neutral']
# print(len(combinedFaction.cards))
# print(self.leader.__dict__.items())


for card in leaders:
    if 'special' in card.info.lower():

        print(card.name)
        print(card.faction)
        print(card.info)



# todo: the card set is incomplete

# todo: labels are also not complete, unless derived

# C:\Program Files (x86)\GOG Galaxy\Games\Gwent\Gwent_Data\StreamingAssets

