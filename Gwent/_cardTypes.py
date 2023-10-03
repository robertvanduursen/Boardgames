""" factions and other descriptions """


class Neutral:
	""" Neutral faction"""
	setSize = 190
	cards = 190
	Leaders = 0
	Units = 105
	Spells = 69
	Artifacts = 15
	Strategems = 1

	# 251 keywords
	# 29 abilities
	keywords = {
		'deploy' : 82,
		'order' : 24,
		'melee' : 19,
		'ranged' : 17,
		'zeal' : 11,
		'summon' : 10,
		'doomed' : 9,
		'banish' : 8,
		'deathblow' : 8,
		'spawn' : 8,
		'lock' : 7,
		'charge' : 6,
		'cooldown' : 6,
		'shield' : 6,
		'create' : 4,
		'purify' : 4,
		'resilient' : 4,
		'reset' : 3,
		'bleeding' : 2,
		'poison' : 2,
		'reveal' : 2,
		'vitality' : 2,
		'deathwish' : 1,
		'discard' : 1,
		'drain' : 1,
		'heal' : 1,
		'immune' : 1,
		'seize' : 1,
		'spying' : 1,
	}


class Syndicate:
	""" Syndicate faction"""
	setSize = 98
	cards = 98
	Leaders = 6
	Units = 73
	Spells = 18
	Artifacts = 1
	Strategems = 0

	# 239 keywords
	# 32 abilities
	keywords = {
		'deploy' : 35,
		'profit' : 26,  # unique
		'coin' : 22,  # unique
		'fee' : 19,  # unique
		'tribute' : 15,  # unique
		'spawn' : 13,
		'summon' : 13,
		'melee' : 12,
		'ranged' : 12,
		'order' : 9,
		'intimidate' : 8,  # unique
		'cooldown' : 6,
		'bounty' : 5,  # unique
		'deathblow' : 5,
		'hoard' : 5,  # unique
		'insanity' : 4,  # unique
		'poison' : 4,
		'shield' : 4,
		'bleeding' : 3,
		'bonded' : 3,
		'charge' : 3,
		'purify' : 2,
		'vitality' : 2,
		'banish' : 1,
		'doomed' : 1,
		'duel' : 1,
		'heal' : 1,
		'immune' : 1,
		'lock' : 1,
		'resilient' : 1,
		'seize' : 1,
		'zeal' : 1,
	}


class Nilfgaard:
	""" Nilfgaard faction"""
	setSize = 90
	cards = 90
	Leaders = 6
	Units = 74
	Spells = 9
	Artifacts = 1
	Strategems = 0

	# 164 keywords
	# 23 abilities
	keywords = {
		'deploy' : 58,
		'melee' : 16,
		'ranged' : 15,
		'order' : 14,
		'spying' : 9,
		'lock' : 6,
		'charge' : 5,
		'create' : 5,
		'spawn' : 5,
		'reveal' : 4,
		'seize' : 4,
		'summon' : 4,
		'assimilate' : 3,  # Assimilate: Boost self by 1 whenever you play a card that is not from your starting deck.
		'shield' : 3,
		'banish' : 2,
		'deathblow' : 2,
		'poison' : 2,
		'purify' : 2,
		'bleeding' : 1,
		'doomed' : 1,
		'heal' : 1,
		'reset' : 1,
		'zeal' : 1,
	}


class Monster:
	""" Monster faction"""
	setSize = 93
	cards = 93
	Leaders = 6
	Units = 75
	Spells = 11
	Artifacts = 1
	Strategems = 0

	# 181 keywords
	# 25 abilities
	keywords = {
		'deploy' : 42,
		'deathwish' : 20,
		'summon' : 14,
		'melee' : 13,
		'order' : 12,
		'spawn' : 10,
		'thrive' : 10,  # Thrive: Boost this unit by 1 whenever you play an ally with higher power.
		'bleeding' : 9,
		'consume': 9,  # Consume: Eat a unit and boost by its power. If it's on the battlefield, destroy it. If in hand or deck, move it to the graveyard. If in the graveyard, remove it from the game.
		'dominance' : 7,  # Dominance: Trigger this ability if you control another unit with the highest power on the battlefield.
		'ranged' : 6,
		'charge' : 5,
		'doomed' : 5,
		'cooldown' : 3,
		'immune' : 3,
		'drain' : 2,
		'purify' : 2,
		'zeal' : 2,
		'banish' : 1,
		'bonded' : 1,
		'create' : 1,
		'deathblow' : 1,
		'seize' : 1,
		'shield' : 1,
		'vitality' : 1,
	}


class Northern_Realms:
	""" Northern Realms faction"""
	setSize = 89
	cards = 89
	Leaders = 6
	Units = 73
	Spells = 9
	Artifacts = 1
	Strategems = 0

	# 206 keywords
	# 26 abilities
	keywords = {
		'order' : 41,
		'deploy' : 32,
		'charge' : 18,
		'zeal' : 15,
		'melee' : 13,
		'formation' : 10,  # Formation: If played on the melee row, gain Zeal. If played on the ranged row, boost self by 1.
		'ranged' : 9,
		'inspired' : 8,  # Inspired: Trigger this ability if this unit's current power is higher than its base power.
		'shield' : 8,
		'deathblow' : 7,
		'summon' : 7,
		'spawn' : 6,
		'cooldown' : 5,
		'vitality' : 5,
		'bleeding' : 4,
		'resupply' : 4,  # Resupply: Trigger this ability whenever you play a Warfare card.
		'crew' : 3,  # Crew: Trigger this ability if this unit is between two Soldiers.
		'duel' : 2,
		'spying' : 2,
		'bonded' : 1,
		'create' : 1,
		'deathwish' : 1,
		'lock' : 1,
		'purify' : 1,
		'reset' : 1,
		'resilient' : 1,
	}



class Scoiatael:
	""" Scoiatael faction"""
	setSize = 98
	cards = 90
	Leaders = 6
	Units = 71
	Spells = 7
	Artifacts = 6
	Strategems = 0

	# 177 keywords
	# 25 abilities
	keywords = {
		'deploy' : 47,
		'order' : 23,
		'melee' : 21,
		'ranged' : 19,
		'zeal' : 8,
		'ambush' : 6,  # Ambush: Played face down, then flips over when the ability's condition is met.
		'cooldown' : 6,
		'charge' : 5,
		'harmony' : 5,  # Harmony: Boost self by 1 whenever you play a Scoia'tael unit on your side whose primary category is unique among other allied Scoia'tael units.
		'poison' : 4,
		'spawn' : 4,
		'summon' : 4,
		'vitality' : 4,
		'deathblow' : 3,
		'immune' : 3,
		'shield' : 3,
		'heal' : 2,
		'lock' : 2,
		'purify' : 2,
		'bleeding' : 1,
		'bonded' : 1,
		'create' : 1,
		'doomed' : 1,
		'resilient' : 1,
		'reveal' : 1,
	}

class Skellige:
	""" Skellige faction"""
	setSize = 92
	cards = 92
	Leaders = 6
	Units = 75
	Spells = 10
	Artifacts = 1
	Strategems = 0

	# 167 keywords
	# 23 abilities
	keywords = {
		'deploy' : 47,
		'order' : 20,
		'melee' : 15,
		'bloodthirst' : 10,  # Bloodthirst: Number of damaged enemy units required to trigger this ability.
		'ranged' : 10,
		'summon' : 9,
		'discard' : 7,
		'heal' : 7,
		'spawn' : 7,
		'berserk' : 6,  # Berserk: Trigger this ability whenever base power is equal to or lower than the specified amount.
		'charge' : 6,
		'cooldown' : 4,
		'doomed' : 4,
		'zeal' : 4,
		'bleeding' : 2,
		'lock' : 2,
		'banish' : 1,
		'bonded' : 1,
		'create' : 1,
		'deathblow' : 1,
		'deathwish' : 1,
		'purify' : 1,
		'vitality' : 1,
	}

factions = [Skellige]