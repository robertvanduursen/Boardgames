import sys
sys.path.append(r"C:\Users\rober\Google Drive\Games\Keyforge\data")
#import deck_1


#test = [item for item in deck_1.actions.__dict__.keys() if item[0] != '_']
test = ['Play', 'This', 'Card', 'Creature', 'Artifact', 'Action', 'Upgrade', 'House', 'Key', 'Forge', 'Armor', 'Power', 'Reap', 'Damage', 'Draw', 'Deal', 'Search', 'Destroy', 'Discard', 'Fight', 'Swap', 'Attack', 'Hazardous', 'Taunt', 'Chain', 'Elusive', 'Use', 'Steal', 'Archive', 'Flank', 'Omni', 'Absorb', 'Add', 'Reveal', 'Capture', 'Purge', 'Sacrifice', 'Stun', 'Heal', 'Splash', 'Skirmish', 'Assault', 'Destroyed', 'Neighbor', 'Turn', 'Hand', 'Deck', 'Refills', 'Return', 'Ready', 'Choose', 'Current', 'Exhaust', 'Friendly', 'Opponent', 'Enemy', 'First', 'May', 'Gain', 'Aember', 'Time', 'Dealt', 'Get', 'Skip', 'After', 'During', 'Next', 'Cost', 'Enter', 'Active', 'Lose', 'If', 'You', 'Remainder', 'Word', 'Zone', 'Unforge', 'Trigger', 'Trait', 'Target', 'Template', 'Take', 'Shuffle', 'Repeat', 'Poison', 'Pick', 'Pay']
test = [x.lower() for x in test]
'''
for x in test:
    test.remove(x)
    if any([x in y for y in test]):
        print(True,'for',x)
        print([y for y in test if x in y])
'''

text = """
If a creature with the assault (X) keyword gains another instance of the
assault (X) keyword, the two X values are added together.
ATTACK, ATTACKER, ATTACKING
See “Fight” on page 10.
BATTLELINE
The battleline is the ordered line of creatures a player controls in play.
See “Creatures” on page 6.
BEFORE
If the word “before” is used in an ability (for example, “Before Reap:” or
“Before Fight:”), that ability resolves before resolving the game effect of
the reap or fight (but after the card exhausts, if exhausting is required to
use the card).
CAPTURE
Captured Æmber is taken from an opponent’s Æmber pool and placed
on a creature controlled by the capturing player. Players may not spend
captured Æmber.
When a creature with Æmber on it leaves play, the Æmber is placed in
the opponent’s Æmber pool.
Unless otherwise specified, Æmber is placed on the creature that
captured it.
CHAIN, CHAINS
Some card abilities cause a player to gain one or more chains. If a player
gains chains, that player increases their chain tracker by the number of
chains gained.
If a player has at least one chain when refilling their hand, they draw
fewer cards according to the chart below. Then, they shed one chain by
reducing the number on their chain tracker by one.
Chains 1-6: draw one fewer card.
Chains 7-12: draw two fewer cards.
Chains 13-18: draw three fewer cards.
Chains 19-24: draw four fewer cards.
See ”Chains” on page 8.
CONTROL
A player owns the cards that begin the game in their deck. When a card
enters play, it is under its owner’s control.
A player can take control of an opponent’s card. When this happens,
that card is placed in the new controller’s play area. If it is a creature, it is
placed on a flank of the new controller’s battleline.
If a player takes control of a card that belongs to a house not in the new
controller’s deck, they can make that house the active house during step
2 of their turn.
If a card that has changed control leaves play for any reason, it moves to
its owner’s appropriate out-of-play zone.
COST, AT CURRENT COST
The base cost to forge a key is six Æmber. This cost may be modified by
card abilities. The modified cost is referred to as the current cost.
DAMAGE
Damage a creature has taken is tracked by placing damage tokens on
the creature. If a creature has an amount of damage on it equal to or
greater than its power, the creature is destroyed. Damage on a creature
does not reduce its power.
For more details on damage and combat, see page 7.
GLOSSARY
This Glossary includes a number of concepts and terms players may
encounter while playing the game, in alphabetical order. Instead of
reading this section from beginning to end, players are encouraged to
only look up new concepts as they are encountered during play.
ABILITY, CARD ABILITY
An ability is the special game text a card contributes to the game.
Unless an ability explicitly references an out-of-play area (such as a hand,
deck, archives, or discard pile), that ability can only interact with cards
that are in play.
ACTION ABILITY
To use an “Action:” ability during their turn, the active player must
exhaust the card. The ability then resolves.
ACTIVE HOUSE
The active house is the house that the active player has chosen for the
current turn.
ACTIVE PLAYER
The active player is the player taking the current turn. The active player
makes all necessary decisions for all card abilities or timing conflicts that
need to resolve during their turn.
ÆMBER
Æmber is tracked by Æmber tokens, and is used to
forge keys.
See also: Capture, Keys, Reap, Steal.
ARCHIVES
A player’s archives is a facedown game area in front of that player’s
identity card. Card abilities are the only means by which a player is
permitted to add cards to their archives. During step 2 of a player’s turn,
after they select an active house, the active player is permitted to pick up
all cards in their archives and add those cards to their hand.
Cards in a player’s archives are considered out of play.
A player may look at their archives at any time. A player is not permitted
to look at an opponent’s archives.
If the ability instructing a player to archive a card does not specify where
the card is archived from, the archived card comes from that player’s hand.
ARMOR
Some creatures have an armor value to the right of the card title. Armor
prevents an amount of damage equal to the armor value that the creature
would take each turn. For example, if a creature has two armor and is dealt
one damage, that damage is absorbed by the armor, leaving the creature
with one armor for the rest of the turn. If the creature is later dealt three
more damage during that turn, one damage is absorbed and the other
two damage are dealt to that creature.
If a creature gains armor, the gains are additive and accumulate on top of
the creature’s printed armor value.
If a creature gains armor during a turn, the gained armor does not
absorb damage already dealt that turn. If a creature loses armor during
a turn, it is not retroactively dealt damage that was already absorbed by
the armor.
If a creature has a “~” symbol in its armor field, the creature has no
armor. Such creatures may gain armor through card effects.
ASSAULT (X)
When a creature with the assault (X) keyword attacks, it deals damage
equal to its assault value (i.e., “X”) to the creature it is fighting before the
fight resolves. (The active player chooses whether this occurs before or
after other “Before Fight” effects and keywords.) If this damage destroys
the other creature, the rest of the fight does not occur.
Æmber Token
KEYFORGE RULEBOOK 10
the hazardous (X) keyword, the two X values are added together.
HEAL
If an ability “heals” a creature, remove the specified amount of damage
from the creature.
If an ability “fully heals” a creature, remove all damage from the creature.
HOUSE CHOICE
Each turn, a player must choose one of the three houses indicated by
their identity card, if able. Some card abilities may restrict a player’s
house choice.
If a player has gained control of a card that does not belong to one of
their three houses, that card’s house becomes an eligible choice for that
player while the player retains control of the card.
If there is no legal choice of house, the player plays the turn with no
active house.
If a player is faced with two (or more) “must choose” mandates, the
player may choose either of those options.
“IF YOU DO” AND “IN ORDER TO”
If an ability includes the phrase “if you do” or “in order to,” the player
referenced by the ability must successfully and completely resolve the
text that precedes that phrase before they can resolve or perform the
text that follows that phrase. In other words, if the first part of the ability
is not successfully and completely resolved, that which follows the phrase
does not resolve or cannot be performed.
KEYS
The first player to forge all three of their keys immediately wins
the game.
The color of a key has no impact on the game. Future card abilities may
reference keys of a specific color.
For details on forging keys, see page 4.
LEAST POWERFUL
A reference to the “least powerful” creature refers to the creature in play
with the lowest power. If there are multiple creatures that qualify, each is
considered “least powerful.”
If an ability requires the selection of a single least powerful creature, and
multiple creatures are tied, the active player chooses one.
LEAVES PLAY
If a card that is in play leaves play (is returned to hand or deck,
destroyed, discarded, archived, or purged), all non-Æmber tokens and
status cards on the card are removed, all upgrades on the card are
discarded, and all lasting effects applied to the card expire.
If a creature with Æmber on it leaves play, the Æmber is returned to the
opponent’s Æmber pool. If a non-creature card with Æmber on it leaves
play, the Æmber is returned to the general token pool.
If a card has a “Leaves Play:” ability, the effect happens automatically
immediately before the card leaves play.
MAVERICK
This symbol indicates that a card is a maverick. A maverick
is an extremely rare instance of a card that has left its
standard house and is now a part of a new house. For all
game purposes, treat a maverick as belonging to the house
printed on its graphic template.
MAY
If an ability includes the word “may,” the text that follows “may” is
optional. If a player chooses to resolve a “may” ability, the player
must resolve as much of the ability as they
are able.
DESTROYED
When a card is destroyed, it is placed in its owner’s discard pile.
If a card has a “Destroyed:” ability, the effect resolves automatically
when the card is destroyed, immediately before it leaves play.
DISCARD PILE
When a card is destroyed or discarded, it is placed on top of its owner’s
discard pile. The cards in each player’s discard pile are open information,
and may be referenced at any time.
The order of cards in a player’s discard pile is maintained during play,
unless a card ability causes this order to change.
When a player runs out of cards in their deck, they shuffle their discard
pile to create a new deck.
ELUSIVE
The first time a creature with the elusive keyword is attacked each turn, it
is dealt no damage and deals no damage to the attacker in the fight.
Elusive only stops damage that would be dealt by each creature’s power;
damage dealt by keywords or other abilities still applies.
END OF TURN
End of turn effects are resolved when a player’s turn is over—after step 5,
the “Draw Cards” step.
ENEMY
If a card ability refers to an “enemy” game element, it refers to an
element currently controlled by the opponent.
FIGHT
When a player uses a creature to fight, the player exhausts the creature
and chooses an opponent’s creature. Both creatures deal an amount of
damage equal to their power value to the opposing creature in the fight,
and both are “fighting” for the purposes of card effects.
A creature used to fight is said to be “attacking” and can be referred to
as “the attacker” during that fight.
If the attacker is not destroyed, all “Fight:” abilities on the attacking
creature then resolve. If either creature in a fight has a constant ability
referencing the end of the fight (example: “after an enemy creature is
destroyed fighting this creature…”), the creature must survive the fight to
resolve the ability. Only the attacker can trigger “Fight:” abilities.
“FIGHT WITH”
If an ability instructs a player to “fight with” or “ready and fight with”
a creature, the ability is granting the player permission to use the
designated creature to fight. The fight is resolved following the standard
rules for fighting, against a creature controlled by the opponent.
FLANK
The creatures on the far right and far left of a player’s battleline are on
the flanks of the line. A creature in this position is referred to as a flank
creature. Any time a creature enters play or changes control, the active
player chooses which flank of its controller’s battleine it is placed on.
FORGE
For details on forging keys, see page 4.
FRIENDLY
If a card ability refers to a “friendly” game element, it refers to an
element currently under the control of the same player.
HAZARDOUS (X)
When a creature with the hazardous X keyword is attacked, it deals X
damage to the attacking creature before the fight resolves. (The active
player chooses whether this occurs before or after other “Before Fight”
effects and keywords.) If this damage destroys the other creature, the
rest of the fight does not occur.
If a creature with the hazardous (X) keyword gains another instance of
KEYFORGE RULEBOOK 11
PURGE
When a card is purged, it is removed from the game and placed
facedown beneath its owner’s identity card. Purged cards no longer
interact with the game state in any manner.
RARITY
A card’s rarity symbol can be found at the bottom of the card, near the
collector number. A card’s rarity (common, uncommon, rare, or special)
is used by the deck-generation algorithm to determine how frequently
it will appear in decks. Special cards have a different type of distribution
and do not obey the game’s standard rarity rules.
REAP
When a player uses a creature to reap, the player exhausts the creature,
gains 1 Æmber for their Æmber pool, and then all “Reap:” abilities on
the creature resolve.
RETURN
When captured Æmber is returned, it is placed in the opponent’s Æmber
pool.
SACRIFICE
When a player is instructed to sacrifice a card, that player must discard
that card from play.
When a card is sacrificed, that card is considered to have been
destroyed, and any “Destroyed:” abilities the card has resolve.
SEARCH
When a player searches a game area (such as a deck), that player looks
at all the cards in the specified area without showing those cards to the
opponent. A player may choose to fail to find the object of a search.
If an entire deck is searched, the deck must be adequately shuffled upon
completion of the search.
If a discard pile is searched, the cards are kept in the same order.
SELF-REFERENTIAL TEXT
If a card’s ability refers to its own title, that reference is only to itself and
not to other copies of the card.
SKIRMISH
When a creature with the skirmish keyword is used to fight, it takes no
damage from the opposing creature when the damage from the fight
is dealt.
This applies only to damage that would be dealt by the opposing
creature’s power, not by damage that is dealt by keywords or other
card abilities.
SPLASH
When an ability deals damage to a creature “with splash damage,” the
splash damage is dealt to each of the target creature’s neighbors.
STEAL
When an ability steals Æmber, the stolen Æmber is removed from the
opponent’s Æmber pool and added to the Æmber pool of the player
resolving the steal ability.
If an ability steals more Æmber than a player has remaining in their pool,
the ability steals only the amount remaining in the pool.
MOST POWERFUL
A reference to the “most powerful” creature refers to the creature in play
with the highest power. If there are multiple creatures that qualify, each is
considered “most powerful.”
If an ability requires the selection of a single most powerful creature,
and multiple creatures are tied, the active player chooses among the
tied creatures.
MULLIGAN
During setup, each player, starting with the first player, has one
opportunity to mulligan their starting hand. This is done by shuffling the
starting hand back into the deck and drawing a new starting hand with
one fewer card in it.
After a player chooses to mulligan, that player must keep the new
starting hand.
NEIGHBOR
The creatures to the immediate left and right of a creature in a player’s
battleline are its neighbors.
OMNI
The active player may trigger any ”Omni:“ abilities under their control
during any of their turns, even if the card with the ”Omni:“ ability does
not belong to the active house.
OFF HOUSE
An off house card is any card that belongs to a house that is not the
active house.
OPPOSING
When a creature is involved in a fight (either because it was used to fight,
or because it was attacked by another creature), the other creature in the
fight is the opposing creature.
PAY
If a player must pay Æmber to an opponent, the Æmber is removed from
the paying player’s pool and added to the opponent’s pool.
PLAY
When a card has a “Play:” ability, the effect occurs any time the card
is played. For creatures, artifacts, and upgrades, the ability resolves
immediately after the card enters play. For action cards, the ability
resolves, and then the card is placed in its owner’s discard pile.
If an ability “plays” a card from a source other than hand, “Play:”
abilities on the card resolve. If an ability “puts” a card “into play,”
“Play:” abilities on the card do not resolve.
POISON
Any damage dealt via the power of a creature with the poison keyword
during a fight destroys the damaged creature. This occurs when the
damage is successfully applied to the opposing creature.
Poison has no effect if all of the damage is absorbed by armor or
prevented by another ability—poison only resolves when one or more
damage is successfully dealt.
Poison refers only to damage that would be dealt by the creature’s
power, not by damage that is dealt by keywords or other card abilities.
POWER COUNTER +1, POWER STATUS CARD
When a creature is given a “+1 power counter,” one such status card is
placed on the creature. For each of these cards that is on a creature, that
creature’s power is increased by one.
PRECEEDING, REPEAT THE PRECEEDING
If card text instructs players to repeat a preceeding effect, the entirety
of the effect before the text providing the instruction to repeat
resolves again.
Common
Uncommon
Rare
Special
KEYFORGE RULEBOOK 12
“THIS WAY”
If an ability refers to an effect that occurred “this way,” it is referring to
an effect that was produced by the same resolution of that same ability.
TURN
A turn consists of one player performing the five steps detailed in the
game’s turn sequence, which are:
1 Forge a key.
2 Choose a house.
3 Play, discard, and use cards of the chosen house.
4 Ready cards.
5 Draw cards.
TRAITS
Traits are descriptive attributes (such as “Knight” or “Specter”) that may
be referenced by other cards. Traits are listed at the top center of a card’s
text box.
Traits have no inherent game effect, but may be referenced by
card abilities.
UNFORGE
If a previously forged key is “unforged,” flip the key token to its unforged
side. The key no longer counts toward its controller’s victory condition
and must be forged again to win the game.
USE
See “Using Cards” on page 6.
"""
text = text.lower()
for x in r':”".,!\',“\'()1234567890~’+-;':
    text = text.replace(x,'')
for idx,x in enumerate(sorted(set(text.split()))):
    if not any([y in x for y in test]):
        print(x.capitalize())
    else:
        pass