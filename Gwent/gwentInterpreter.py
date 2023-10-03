"""

an interpreter for the mechanics of Gwent: Iron Judgement

i.e
effect of card = +(5+2 boost) to score at optimal play -> max
                    +5 at normal play -> min

"""

import gwentData, random, re

keyWords = [
    ('ambush', "Ambush: Played face down, then flips over when the ability's condition is met.") ,
    ('armor', 'Armor: Absorbs a given amount of damage, then is removed.') ,
    ('assimilate', 'Assimilate: Boost self by 1 whenever you play a card that is not from your starting deck.') ,
    ('aura', 'Aura: Passive ability that is undone when the unit is destroyed or Locked.') ,
    ('banish', 'Banish: Remove from the game. Note: Does not count as being destroyed.') ,
    ('banish_in_graveyard', "Doomed: Units: Remove from the game when moved from the Board to the Graveyard.\\nSpecial Cards: Remove from the game after triggering the card's ability.") ,
    ('berserk', 'Berserk: Trigger this ability whenever base power is equal to or lower than the specified amount.') ,
    ('bleeding', 'Bleeding: Status that damages this unit by 1 on its turn end. Note: Bleeding turns can accumulate; 1 turn of Bleeding cancels out 1 turn of Vitality.') ,
    ('bloodthirst', 'Bloodthirst: Number of damaged enemy units required to trigger this ability.') ,
    ('bond', 'Bonded: Trigger this ability if you control a copy of this card.') ,
    ('bonded', 'Bonded: Trigger this ability if you control a copy of this card.') ,
    ('boon', 'Boon: Positive row effect. Replaced by other row effects and removed on round end.') ,
    ('boost', "Boost: Increase a Unit's current Power.") ,
    ('boosted', "Boosted: A Boosted Unit's current Power is more than its base Power.") ,
    ('bounty', 'Bounty Status: Whenever a unit with this status is destroyed, opponent gains coins equal to its base power. Bounty can only be placed on one enemy unit at any given time.') ,
    ('brave', 'Brave: Trigger this ability if your opponent is winning the current Round (calculated after placing this Unit and any Units it Spawns).') ,
    ('charge', 'Charge: The number of times an Order ability can be used. Only cards with Charge: X can gain additional Charges.') ,
    ('charm', 'Charm: Move an enemy to the opposite row.') ,
    ('clone', 'Clone: An exact copy of a card, with the same current Power and abilities.') ,
    ('coin', "Coin: The Novigradian underworld's currency of choice for paying Fees and Tributes. You may possess a maximum of 9 Coins. Your Coin-count is reduced by half (rounded down) when carried over into the next round.") ,
    ('collateral', 'Collateral: If you have insufficient Crowns, damage this unit by the number of Crowns required to Spend to trigger its ability.') ,
    ('conceal', 'Conceal: Turn over a face-up card in hand.') ,
    ('consume', "Consume: Eat a unit and boost by its power. If it's on the battlefield, destroy it. If in hand or deck, move it to the graveyard. If in the graveyard, remove it from the game.") ,
    ('cooldown', 'Cooldown: The number of turns before an Order or Fee ability can be reused.') ,
    ('counter', 'Counter: Reduce the Counter whenever the given condition is met. Reset the Counter when the Unit leaves the Board.') ,
    ('cover', 'ignore') ,
    ('craven', 'Craven: Trigger this ability if your opponent is losing the current Round.') ,
    ('create', 'Create: Spawn one of three randomly selected cards from the specified source.') ,
    ('crew', 'Crew: Trigger this ability if this unit is between two Soldiers.') ,
    ('crewed', 'Ignore.') ,
    ('crown', 'Crown: The unit of Novigradian currency required to pay Fees and Tributes. You may possess a maximum of 9 Crowns. Your Crown-count is reduced by half (rounded down) when carried over into the next round.') ,
    ('damage', "Damage: Decrease a Unit's current Power.") ,
    ('damaged', "Damaged: A Damaged Unit's current Power is less than its base Power.") ,
    ('deadlock', 'Clash: Trigger this ability only if neither player has passed.') ,
    ('deathblow', 'Deathblow: Trigger this ability if this card destroys a unit.') ,
    ('deathwish', 'Deathwish: Trigger this ability when destroyed and moved from the battlefield to the graveyard. Note: Banished units are not sent to the graveyard.') ,
    ('demote', "Demote: Convert a Gold card to Silver (or Bronze, if Bronze was the card's original color).") ,
    ('deploy', 'Deploy: Trigger this ability when played.') ,
    ('destroy', 'Destroy: Move the card to the Graveyard.') ,
    ('discard', 'Discard: Move a card from your hand to the graveyard. Note: Related abilities are not triggered when discarding manually.') ,
    ('dominance', 'Dominance: Trigger this ability if you control another unit with the highest power on the battlefield.') ,
    ('doomed', 'Doomed: Status that removes the unit from the game when it leaves the battlefield.') ,
    ('drain', 'Drain: Deal damage and boost self by the same amount.') ,
    ('draw', 'Draw: Move the top card or cards from your Deck to your Hand.') ,
    ('duel', 'Duel: Units take turns dealing damage equal to their power until one of them is destroyed.') ,
    ('enemy', "Enemy: A Unit on your opponent's side of the Board.") ,
    ('fatigue', "Single-Use: This card's ability can be used only once per game.") ,
    ('fee', 'Fee: Trigger this ability by spending the specified number of Coins.') ,
    ('formation', 'Formation: If played on the melee row, gain Zeal. If played on the ranged row, boost self by 1.') ,
    ('friendly', 'Ally: A Unit on your side of the Board.') ,
    ('gamble', 'Gamble: Play a game of chance.') ,
    ('gold', 'Immune: Status whereby this card cannot be targeted.') ,
    ('harmony', "Harmony: Boost self by 1 whenever you play a Scoia'tael unit on your side whose primary category is unique among other allied Scoia'tael units.") ,
    ('hazard', 'Hazard: Negative row effect. Replaced by other row effects and removed on round end.') ,
    ('heal', "Heal: If a unit's current power is lower than its base power, restore it either to base power or by the amount specified.") ,
    ('highest', 'Highest: Highest power, ties are resolved randomly.') ,
    ('hoard', 'Hoard: Trigger this ability if you possess the specified number of Coins or more.') ,
    ('idle', 'Idle: The number of turns a unit must remain on the board before it can be triggered.') ,
    ('immobile', 'Cannot be moved.') ,
    ('immune', 'Immunity: Status whereby this card cannot be manually targeted.') ,
    ('insanity', 'Insanity: If you have insufficient Coins, damage this unit by its Fee amount to trigger its Fee ability. Note: Insanity cannot be used if it would destroy the unit.') ,
    ('inspired', "Inspired: Trigger this ability if this unit's current power is higher than its base power.") ,
    ('intimidate', 'Intimidate: Boost self by 1 or the specified amount whenever you play a Crime card.') ,
    ('leadership', "Leadership: Trigger this ability when either Leader card is played (but before the Leader's ability is resolved).") ,
    ('lock', "Lock: Status that disables a unit's abilities.") ,
    ('lowest', 'Lowest: Lowest power, ties are resolved randomly.') ,
    ('mayhem', 'Mayhem: Boost self by 1 or the specified amount whenever you play a Crime card.') ,
    ('melee', 'Melee: This ability can only be used while on the melee row.') ,
    ('mulligan', 'Mulligan: Shuffle a card from your hand into your deck and draw the top card from your Deck.') ,
    ('muster', 'Summon: Play automatically from the deck.') ,
    ('non_decoyable', 'Stubborn: Cannot be moved back to the hand.') ,
    ('order', 'Order: An ability triggered manually by the player. Cards with Order cannot be used for 1 turn after being placed on the battlefield.') ,
    ('overstrain', 'Effort: Perform the specified action for every card targeted by the preceding ability.') ,
    ('pair', 'Pair: Trigger this ability when 2 copies of this card are present on the Board.') ,
    ('poison', 'Poison: Status - if a unit receives two instances of Poison, destroy it.') ,
    ('profit', 'Profit: Gain a specified number of Coins when this card is played. You may possess a maximum of 9 Coins.') ,
    ('promote', 'Promote: Convert the card to Gold until the Round ends.') ,
    ('purify', 'Purify: Remove all statuses.') ,
    ('ranged', 'Ranged: This ability can only be used while on the ranged row.') ,
    ('reach', 'Reach: The distance in rows that you can target.') ,
    ('regress', 'Regress: Return the card to its original state.') ,
    ('regressing', 'Regressing: When this Unit is removed from the Board, its base Power is returned to the value it has in the Collection. Not disabled by Lock.') ,
    ('reset', 'Reset: Restore a unit to its base power.') ,
    ('resilient', 'Resilience: Status that allows a unit to remain on the board at round end, and if boosted restores it to its base power.') ,
    ('resistant', 'Resistant: A Resistant Unit is not affected by the specified Hazard effect.') ,
    ('restrained', 'Cannot target Bosses.') ,
    ('resupply', 'Resupply: Trigger this ability whenever you play a Warfare card.') ,
    ('resurrect', 'Resurrect: Play from your graveyard.') ,
    ('retaliation', 'Retaliation: Trigger this ability whenever this Unit is Damaged but not sent to the Graveyard.') ,
    ('reveal', 'Reveal: Show a card to both players, then hide it back in the hand or deck.') ,
    ('revealed', 'Revealed: A card in the hand that has been turned over.') ,
    ('revenge', "Revenge: Trigger this ability when the card is moved from the Board to the Graveyard during your opponent's turn.") ,
    ('round_end', 'Round End: Trigger this ability when the Round ends.') ,
    ('seize', 'Seize: Move an enemy to the opposite row.') ,
    ('shield', 'Shield: Status that blocks the next instance of damage dealt to a unit.') ,
    ('solitary', 'Solitary: Trigger this ability if there is only 1 copy of this card on the Board.') ,
    ('spawn', 'Spawn: Add a card to the game.') ,
    ('spend', 'Spend: The amount of Crowns needed to trigger this ability.') ,
    ('spring', 'Spring: Turn over a face down Ambush card and trigger its ability.') ,
    ('spying', 'Spying: Status for a unit played on or moved to the opposite side of the battlefield.') ,
    ('strengthen', 'Strengthen: Increase the base power of a unit.') ,
    ('stubborn', 'Stubborn: Cannot be replayed or returned to the hand.') ,
    ('summon', 'Summon: Move automatically to the battlefield (not considered played).') ,
    ('swap', 'Swap: Move a card from hand to deck and draw another in its place during your turn.') ,
    ('thrive', 'Thrive: Boost this unit by 1 whenever you play an ally with higher power.') ,
    ('timer', 'Timer: Reduce the Timer by 1 every turn while this Unit is on the Board. Trigger the ability when it reaches 0 (at the start or end of the turn). Reset the Timer when the Unit leaves the Board.') ,
    ('token', 'Token: A unit that is removed from the game on round end.') ,
    ('transform', 'Transform: Convert into a different card.') ,
    ('tribute', 'Tribute: On Deploy, you may choose to spend the specified amount of Coins to trigger this ability.') ,
    ('trio', 'Trio: Exactly 3 Unlocked copies of a Unit on a row.') ,
    ('truce', 'Truce: If neither player has passed.') ,
    ('turn_end', 'Turn End: Trigger this ability at the end of your turn.') ,
    ('turn_start', 'Turn Start: Trigger this ability at the start of your turn.') ,
    ('veteran', 'Veteran X: At the start of Rounds 2 and 3, Strengthen this Unit by X, wherever it is.') ,
    ('vitality', 'Vitality: Status that boosts this unit by 1 on its turn end. Note: Vitality turns can accumulate; 1 turn of Vitality cancels out 1 turn of Bleeding.') ,
    ('weaken', 'Weaken: Decrease the base power of a unit. If it falls below 1, remove it from the game. Does not trigger Deathwish abilities.') ,
    ('zeal', 'Zeal: An Order ability can be used on the same turn the card is placed on the battlefield.') ,
]


# for idx, word in enumerate(keyWords):     print(idx)

'''
NOTE

The interpreter stack even extends to cards in the graveyard and deck
I.e. this means that cards must always be parsed for state
Should this be stored on the card?
The players Deck? Should be able to query cards of the other player's


'''

triggers = [
    ('in this row', 'play on same row'),
    ('instead', 'place previous ability'),
    ('other', 'requires other creature'),
]

tokens = [card for card in gwentData.allCards if 'Token' in card.categories]


class cardInterpreter:
    """ an attempt to AT LEAST figure out the pre and post state of the board for this card """
    words = list
    card = False
    tokens = False
    abilities = False

    def __init__(self, card):
        self.card = card
        self.text = card.info
        self.words = []
        self.tokens = []
        self.abilities = []

        print('processing card %s' % card.name)

    def labelWords(self):
        """ find and mark the known words """
        print(self.text)
        for word, descr in keyWords:
            if word in self.text.lower():
                print('"%s" found' % word)
                print(re.search(r"%s(.*)" % word, self.text.lower()).groups())
                print()
                self.abilities.append(word)

        for word, descr in triggers:
            if word in self.text.lower():
                print(word, 'found')
                self.words.append(word)

        for card in tokens:
            if card.name.lower() in self.text.lower():
                print(card.name, 'found')
                self.tokens.append(card)


        ''' 
        are abilities always delimited by a dot (i.e. a sentence)?
        do all abilities stay on 1 sentence / line?
        '''

    def constructExecutionOrder(self):
        """ construct a valid execution order """

        # i.e. Eval = Deploy( Armor( card.unit ))

    def runEffects(self):
        """ eval the Exec Order and label the results """

        # i.e. score was 0; score is 5 after eval

        '''
        do we construct valid Python code to run?
        -> this would allow the running of conditional logic 
        
        or "simple" text matching to outcomes
        '''

        tokenValues = [token.strength for token in self.tokens]
        return self.card.strength + sum(tokenValues)


def specialCard():
    """ card sent to the graveyard after use """



faction = gwentData.Factions['Scoiatael']

bootCards = [card for card in faction.cards if 'boost' in card.info.lower()]
# testCard = faction.getCard('Dwarven Chariot')
testCard = bootCards[1]



'''
Dwarven Chariot
Deploy: Spawn a Rowdy Dwarf in this row.
Bonded: Spawn 2 Rowdy Dwarves in this row instead.
'''

interp = cardInterpreter(testCard)
interp.labelWords()
print(interp.runEffects())

'''

to process the 'when this happens' effects, you need a way to list slots that trigger at said stage
you need a stage machine

'''