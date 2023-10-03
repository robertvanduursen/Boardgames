"""

do I use this file for more than just Descriptors?


"""

class identityCard:
    pass


class _Rig:
    pass


class Runner:
    """ the Runner """

    identity = identityCard

    Grip = 'hand'
    # Rig = 'equipment'
    Stack = 'deck'
    Heap = 'discard pile'

    scoreArea = 'place'
    creditPool = 'place'
    clickMarker = 'place'

    def __init__(self):
        pass

    @property
    def Rig(self) -> _Rig:
        return _Rig


    def run(self):
        """ do a Run """

        # a Run is an emergent sequence
        pass

    def receiveDamage(self):
        """
            The Runner can receive the following 3 types of damage:
    Meat, Net, Brain
        :return:
        """

    def playArea(self):
       '''

       Runner Play Area
       In addition to his credit pool, identity card, score area, and click
       tracker, the Runner’s play area includes his grip, his stack, his
       heap, and his rig.
       Grip
       This is the Runner’s hand of cards. The Runner begins the game
       with a maximum hand size of five cards. Cards in the grip are
       inactive.
       Stack
       This is the Runner’s draw deck. The stack is kept facedown
       within reach of the Runner. Cards in the stack are inactive.
       Heap
       This is the Runner’s trash pile. The heap is kept adjacent to the
       Runner’s identity card. This is where Runner cards are placed
       when they are trashed or discarded. Cards in the heap are
       faceup and inactive. Both the Runner and Corporation may
       look through the heap at any time, but must maintain the order
       of its cards.
       Rig
       This is where the Runner installs his cards. The rig is separated
       into three rows: one for programs, one for hardware, and one
       for resources. Cards in the rig are active.


       '''

class Coorporation:
    """ the Corp """

    identity = identityCard

    RnD = 'hand'
    servers = identityCard
    root = 'deck'
    HQ = root + identity
    Archives = 'discard pile'

    scoreArea = 'place'
    creditPool = 'place'
    clickMarker = 'place'


    def __init__(self):
        pass



    @property
    def icepieces(self):
        """ a Handle for the pieces of Ice the Corp has """
        return []


    def playArea(self):
        """

'''

Corporation Play Area
In addition to his credit pool, identity card, score area, and click
tracker, the Corporation’s play area includes his servers and
his ice. There are two types of servers: central servers and
remote servers.
Central Servers
The Corporation has three central servers: Headquarters,
Research and Development, and Archives. Each central
server also has a root.
Headquarters (HQ)- This is the Corporation’s hand of
cards. Cards in HQ are inactive. The Corporation begins the
game with a maximum hand size of five cards. The Corporation
identity card represents HQ for the purposes of card
installation.
Research and Development (R&D)-
This is the Corporation’s draw deck. R&D is kept facedown
within reach of the Corporation. Cards in R&D are inactive.
Archives- This is the Corporation’s trash pile. Archives is
kept adjacent to R&D. This is where Corporation cards are
placed when they are trashed or discarded. Cards in
Archives are inactive.
Some cards enter Archives faceup, and some cards enter
Archives facedown. Facedown cards in Archives should be
oriented horizontally so that the Runner can easily see them.
Both the Corporation and Runner may look through the
faceup cards stored in Archives at any time, and do not need to
maintain the order of its cards while doing so. The Corporation
can also look at the facedown cards in Archives at any time; the
Runner cannot.
Root- This is the area of a central server where upgrades
for the server are installed. When an upgrade is installed in the
root, it should be placed below the server. If a root has no cards
installed in it, it is considered to be empty.
Remote Servers
The Corporation has no remote servers at the beginning of the
game. The Corporation creates remote servers by installing
cards. Cards in remote servers are active if rezzed and inactive
if unrezzed.
There is no limit to the number of remote servers the
Corporation can have at any given time.
Ice
The Corporation installs ice to protect his servers. Installed ice
is always dedicated to a particular server and placed in front
of that server. Ice can protect an empty serve

 and placed in front
of that server. Ice can protect an empty server. Ice is active if
rezzed and inactive if unrezzed.

'''
        :return:
        """


class Run:
    """ """

    def initiation(self):
        pass

    def confrontation(self):
        pass

    def access(self):
        pass



    """
    
    Runs
    Runs are the heart of Android: Netrunner, and provide
    opportunities for the Runner to steal the Corporation’s agendas
    and trash his cards. In a run, the Runner attacks one of the
    Corporation’s servers in an attempt to access cards, using his
    installed programs to help him pass the Corporation’s ice.
    Because most runs pit the Runner’s installed icebreaker
    programs against the Corporation’s installed ice, it is vital that
    both players understand the functions and subtypes of the
    Corporation’s ice and the Runner’s icebreakers.
    Ice
    Ice is defensive software the Corporation installs in front of
    his servers to protect his valuable data. There are four main
    subtypes that can appear on a piece of ice: sentry, barrier,
    code gate, and trap. Ice also has separate abilities called
    subroutines.
    Subroutines
    Subroutines are abilities of a piece of ice marked by the |
    symbol. If the Runner encounters a piece of rezzed ice and does
    not or cannot break its subroutines, the unbroken subroutines
    trigger and resolve one by one.
    In addition to preventing the Runner’s access to the
    Corporation’s servers by ending his run, subroutines can
    pose other hazards if allowed to trigger, such as damaging the
    Runner or initiating trace attempts (see “Traces and Tags” on
    page 20).
    Icebreakers
    Icebreakers are programs with the icebreaker subtype that
    the Runner can use to overcome ice encountered during a run.
    Each icebreaker has a strength, an install cost, and one or more
    subtypes that reflect which kind of ice subroutine it is designed
    to break.
    The Runner uses icebreakers to interact with and break
    subroutines on ice. An icebreaker can only interact with ice that
    has equal or lower strength than the icebreaker.
    In addition to this strength requirement, many icebreaker
    abilities can only be used to break subroutines on particular
    subtypes of ice. For example, an icebreaker that has the ability
    “1<: Break barrier subroutine” can only use this ability to break
    subroutines on a piece of ice with the barrier subtype. It does
    not matter if the ice has additional subtypes, provided it has any
    subtypes referred to by the icebreaker’s ability. If an ability does
    not restrict itself to a subtype (i.e., “Break ice subroutine”), it
    can be used against any piece of ice.
    Increasing an Icebreaker’s Strength
    Many icebreakers allow the Runner to temporarily increase the
    icebreaker’s strength by spending credits. This helps the Runner
    deal with stronger pieces of ice, provided he has enough credits
    to spend. This strength increase lasts only while the current
    piece of ice is being encountered, unless otherwise noted
    by card abilities. After an encounter with a piece of ice, the
    icebreaker’s strength returns to the value shown on its card. This
    applies to any other strength modifiers given by icebreakers as
    well.
    """

    """
    Phases of a Run
    Runs typically transpire in three phases. Not every run will
    include all of these phases. Players are encouraged to use the
    following text in combination with the “Timing Structure of
    a Run” diagram on page 33 in order to fully understand the
    intricacies of runs.
    1. Initiation Phase
    2. Confrontation Phase
    3. Access Phase
    1. Initiation Phase
    To initiate a run, the Runner declares the server that he
    is attacking. The Runner can only initiate a run against a
    single server per run action.
    After the Runner declares the server he is attacking, he
    gains 1< to spend during the run for each point of bad
    publicity the Corporation has. Then, both players check to
    see if there is ice protecting the attacked server.
    If there is ice protecting the server, the run proceeds to the
    Confrontation phase.
    If there is no ice protecting the server, the run proceeds to
    the Access phase.
    2. Confrontation Phase
    The Confrontation phase consists of approaching a
    piece of ice and then potentially encountering that
    ice. A Runner approaches each piece of ice protecting the
    server one at a time, starting with the outermost piece. The
    Runner must pass each piece of ice in order to approach
    the next piece of ice protecting the server, continuing until
    all pieces of ice have been passed or until the run ends.
    If the Runner passes all pieces of ice protecting the attacked
    server, the run proceeds to the Access phase.
    Approaching Ice
    When the Runner approaches a piece of ice, he must first decide
    whether he wishes to continue the run or jack out. If he
    decides to jack out, he ends his run and the run is considered
    unsuccessful. The Runner cannot jack out while approaching
    the first piece of ice during a run.
    If the Runner decides to continue instead of jacking out, the
    Corporation has the opportunity to rez the approached piece of
    ice and any other non-ice cards.
    Note: The Corporation can only rez ice when it is approached.
    If the approached piece of ice is rezzed after the Corporation
    has the opportunity to rez cards, then the Runner encounters it.
    If after rezzing cards the approached piece of ice is not rezzed,
    then the Runner passes it. He then continues the run by
    either approaching the next piece of ice protecting the server
    or proceeding to the Access phase if there is no more ice to
    approach.
    Bad Publicity
    Some cards and events in
    Android: Netrunner give the
    Corporation bad publicity. For
    each point of bad publicity
    the Corporation has, the Runner gains 1< at the
    beginning of each run. The Runner may spend these
    credits during his run as if they were in his credit
    pool, but any unspent bad publicity credits return to
    the bank at the end of the run. Bad publicity always
    generates revenue for the Runner at the beginning of
    a run, even when the Runner makes multiple runs in
    a single turn. OUTERMOST
    ICE
    ORDER OF APPROACH
    INNERMOST
    ICE
    Wall of Thorns
    Barrier - AP ICE: | Do 2 net damage. | End the run. Most runners do their business in full-sim, with their rigs wired directly into their brains. The setup has a large number of advantages, with the runner able to process data and input commands far faster than a traditional meat-bound system. But it also means greater
    risk.
    Illus. Adam S. Doyle
    78 © 2012 Wizards of the Coast LLC. © FFG
    8
    5
    Zaibatsu Loyalty
    If the Runner is about to expose a card,
    you may rez Zaibatsu Loyalty.
    1< or ]: Prevent 1 card from being
    exposed.
    Illus. Mike Nesbitt
    ASSET
    © 2012 Wizards of the Coast LLC. © FFG 71
    0
    4
    Approach Example
    REMOTE
    SERVER
    18
    Encountering Ice
    When the Runner encounters a piece of ice, he has the
    opportunity to break any subroutines on that piece of ice. After
    the Runner finishes breaking any subroutines that he wishes
    to break, each unbroken subroutine on that ice triggers in the
    order as listed on the card. If a subroutine ends the run, then
    the run ends immediately and no further subroutines on that
    piece of ice trigger.
    Breaking Subroutines– To break a subroutine, the
    Runner uses abilities on his installed icebreakers. The Runner
    can break the subroutines on the encountered ice in any order
    he chooses. There is no limit to the number of installed cards
    a Runner can use to interact with the encountered ice, but he
    generally only needs one icebreaker. Remember that before
    an icebreaker can interact with a piece of ice, the icebreaker’s
    strength must be equal to or higher than the encountered ice’s
    strength.
    Note: Breaking all subroutines on a piece of ice does not mean
    the ice is trashed. A passed piece of ice remains installed and is
    approached during every subsequent run against the server it
    protects.
    After the Runner breaks all of the ice’s subroutines and/or any
    effects from unbroken subroutines resolve without ending the
    run, he has passed that piece of ice. He then continues the run
    by either approaching the next piece of ice protecting the server
    or proceeding to the Access phase if there is no more ice to
    approach.
    3. Access Phase
    After the Runner has passed all of the ice protecting the
    attacked server, he has one final opportunity to jack out. If he
    chooses to continue, the Corporation has one final opportunity
    to rez cards. After rezzing cards, the run is considered to be
    successful and the Runner accesses the Corporation’s cards
    by looking at them. The type of server attacked determines the
    degree and method of access, and the Runner must access cards
    according to the following rules:
    •	 R&D: The Runner accesses the top card of R&D, and any
    upgrades in its root. Unless the Runner scores, trashes, or is
    forced by a card’s text to reveal the card, he does not show
    cards accessed from R&D to the Corporation.
    •	 HQ: The Runner accesses one random card from HQ and any
    upgrades in its root. Any cards the Runner does not score or
    trash return to HQ.
    •	 Archives: The Runner accesses all cards in Archives and any
    upgrades in its root. The Runner turns all cards faceup when
    accessing them, and does not need to keep them in order. The
    Runner steals all agendas in Archives and cannot trash cards
    that are already in Archives. After accessing Archives, all
    cards in Archives return to Archives faceup.
    •	 Remote Server: The Runner accesses all cards in the server.
    Note: Installed ice is not in a server and is never accessed.
    """

    """
    Accessing Multiple Cards
    When accessing multiple cards, the Runner accesses them one
    at a time in any order he likes. For example, the Runner may
    access a card from HQ, then an upgrade installed in the root of
    HQ, and then another card from HQ, if he has the ability to
    do so.
    When accessing multiple cards from R&D, the Runner must
    draw them in order from the top of the deck, and must return
    any cards not scored or trashed in reverse order, so as to
    preserve their positions in R&D.
    The Runner must fully resolve his access to a card (steal it, pay
    to trash it, etc.) before accessing the next card. If the Runner
    scores an agenda that gives him seven or more points, he
    immediately wins the game, even if he would otherwise access
    more cards.
    Concluding the Run
    After the Runner has accessed all required cards, he returns
    any cards not stolen or trashed to their original play states. For
    example, an unrezzed card in a remote server returns facedown
    to that server, and a card accessed from HQ returns to HQ.
    After a Runner finishes accessing cards, the run ends. The
    Runner returns any unspent bad publicity credits to the token
    bank, and the Runner resumes his Action phase.
    """

class Ice:
    """ the means of protection for the Corp """
    pass

class IceBreaker:
    """ the means of attack for the Runner """
    pass


class terms:
    '''
    Active: An active card’s abilities affect the game and can be
    triggered.
    Inactive: An inactive card’s abilities do not affect the game
    and cannot be triggered.
    Install: This is the game term for playing a card onto the
    table.
    Credit: This is the basic unit of wealth, represented by <.
    Click: This is the basic unit of work, represented by [.
    Rez: This is the act of flipping a facedown card faceup. The
    Corporation installs his cards facedown and must rez them in
    order to use them.
    '''


def verticalRule():
    """
       Agendas, assets, and upgrades are always installed in a
    vertical orientation.
    """

def horizontalRule():
    """
  •	 Ice is always installed in a horizontal orientation.
    """


class Agenda:
    """ d """
    '''
    Stealing Agendas
    If the Runner accesses an agenda, he steals it and places it
    faceup in his score area, resolving any conditional abilities on
    the agenda that use the language “When you steal.” While an
    agenda is in the Runner’s score area, it adds its agenda points
    to his score. The Runner cannot decline to steal agendas he
    accesses.
    '''

    def advance(self):
        """
        Some assets can be advanced.
        Advancing assets gives them the appearance of being agendas.
        This can be useful in bluffing the Runner into making runs which are not beneficial to him.
        """

        # logic : ! All assets can be advanced


class Rezzing:
    """ Rezzed and Unrezzed Cards """

    '''
    The Corporation’s installed cards have two play states:
    
    rezzed: which means that the card is faceup and active, 
    
    and
     
    unrezzed: which means that the card is facedown and inactive. 
    
    The Corporation can look at his unrezzed cards at any time. 
    
    To rez an installed card, the Corporation pays its rez cost and turns the card faceup.
    
    Note: Rezzing a card does not cost the Corporation a click.
    
    To organize this hidden information for both players, it is important that the Corporation observes the
    following rules for card orientation: 
    
        Installed Asset (rezzed)
        Installed Ice (unrezzed)

    '''


class Card:


    def discard(self):
        pass
        '''
        A discarded card is not considered to have been
        trashed, and vice versa. Cards that prevent a card
        from being trashed cannot prevent a card from being
        discarded
        '''


    def trash(self):


        """
        Trashing Cards
        If the Runner accesses a card with a trash cost, he may pay
        credits equal to its trash cost in order to trash it to Archives
        faceup.
        """



class Damage:
    """ Many cards and ice subroutines inflict damage on the Runner. """

    def flatlining(self):
        """ """

        '''
        interesting; does this imply that this means that Runner can have a emptry hand, as long as that is not the case at the end of the turn?
        '''

        return """
            If the Runner takes more damage than the number of cards in
            his grip, OR if he has a maximum hand size of less than zero at
            the end of his turn, then he is flatlined and the Corporation
            wins the game.
        """

    def damageTrashing(self):
        return """
        When the Runner trashes multiple cards for damage, the cards
    are placed in his heap in the order they were randomly trashed.
        """

    def note(self):
        return """ The only differences between net and meat damage are the cards that inflict and prevent them. """

    class Meat:
        """ Meat damage """

        '''
        The Runner randomly trashes one card from
    his grip for each point of meat damage done to him.
        '''

    class Net:
        """ Net damage """

        '''
The Runner randomly trashes one card from
    his grip for each point of net damage done to him.
        '''

    class Brain:
        """ Brain damage """

        '''
The Runner randomly trashes one card
    from his grip for each point of brain damage done to him,
    and his maximum hand size is permanently reduced by one
    card. The Runner takes a brain damage token to track this.
        '''

def winCondition():
    """ Winning the Game """
    # If at any time a player has seven agenda points in his score area,
    # he immediately wins the game.
    for player in [Coorporation, Runner]:
        if player.scoreArea == 7:
            winner = player
            return winner

    # If R&D contains no cards and the Corporation attempts to draw
    # a card, the Runner immediately wins the game.
    if len(Coorporation.RnD) == 0:
        winner = Runner
        return winner

    # If the Runner is flatlined (see “Damage” above), the
    # Corporation wins the game.
    if len(Runner.Grip) == 0:
        winner = Coorporation
        return winner

class Trace:
    def mechanic(self):
        """ Some card abilities initiate a trace on the Runner. """

        '''
        Traces are marked by the language “Trace X” on a card (with X equaling the base trace strength of the trace.) 
        
        Traces pit the Corporation’s trace strength against the Runner’s link strength, both of which are increased by spending credits.
        
        The Corporation acts first during a trace, openly spending any number of credits to increase his trace strength by one point for each credit he spends. 
        There is no limit to the number of credits the Corporation can spend on the trace.
        
        After the Corporation spends his credits, the Runner has the opportunity to openly spend credits to increase his link strength. 
        The Runner’s base link strength is equal to the number of links (~) he has in play.
         
        The Runner increases his link strength by one point for each credit he spends. 
        There is no limit to the number of credits the Runner can spend on the trace.
        
        After the Runner finishes increasing his link strength, it is compared to the Corporation’s trace strength.
        
        If the trace strength exceeds the link strength, the trace is successful and any “If successful” effects associated with the trace are resolved.
        If the link strength is equal to or greater than the trace strength, then the trace is unsuccessful, 
        and any “If unsuccessful” effects associated with the trace are resolved.
        '''

    def example(self):
        """ """
        '''
        A Runner encounters Data Raven & is unable to break the trace subroutine. 
        
        The Runner’s identity card is Kate “Mac” McCaffrey (link of 1) and he has one copy of Access to Globalsec (link of 1) in his rig,
        for a base link strength of 2. 
        
        The Data Raven has a base trace strength of 3, and the Corporation decides to spend 2<, increasing the Data Raven’s trace strength to 5. 
        This means that the Runner would need to spend 3< in order to make the trace unsuccessful. 
        
        The Runner has 7< in his pool and decides to spend 3<, matching the Corporation’s trace strength. 
        Because the trace was unsuccessful, no power counter is placed on Data Raven.
        '''

class Tags:
    """ Though the Corporation spends much of the game repelling
        the Runner’s intrusions, traces and tags give the Corporation
        opportunities to attack the Runner.
    """

    '''
        Certain card effects result in a tag being placed on the Runner. 
        As long as the Runner has at least one tag, he = considered to be tagged. 
        
        While the Runner is tagged, the Corporation may, as an action, spend Click and 2 Credits to trash one of the Runner’s resources. 
        Certain card effects can also trigger off of the Runner being tagged, and it is usually dangerous for the 
        Runner to remain tagged for very long.
        
        While tagged, the Runner may, as an action, spend Click and 2 Credits to remove the tag, returning it to the token bank. 
        The Runner can repeat this action as many times he likes, provided he has the clicks and credits to pay its cost, 
        and as long as he has a tag to remove.

    '''



