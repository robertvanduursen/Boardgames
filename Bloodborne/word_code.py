# -*- coding: utf-8 -*-

import re
from multiprocessing.pool import ThreadPool as Pool
import re,os,sys


'''WORKS OFF OF THE TEXTDUMP FILE'''

localPath = os.environ['USERPROFILE'] + '\\desktop\\Bloodborne_text\\'
readPath = localPath + "textdump.txt"
ins = open(readPath, "r" )
superString = ''
for line in ins.readlines():
    superString += str(line)
ins.close()


''' CONSTRUCT SUPERSTRING '''

superString = superString.replace('\n','')
superString = superString.replace('’','\'')
superString = superString.replace('“','')
superString = superString.replace('”','')
superString = superString.replace('"','')

phrases = {}
for x in superString.split('^'):
    # split at different items
    temp = []
    for y in x.split('#'):
        # split at item name
        for z in y.split('%'):
            # split at in-description line-breaks
            for w in z.split('.'):
                if w != '':
                    temp.append(w.lstrip())
    if len(temp) > 0:
        phrases[temp[0]] = temp[1:]


''' CONSTRUCT WORD FUNCTIONS DICT '''

funcDict = {
'the' : 'next word(s) is entity / noun',
'a' : 'next word(s) is entity / noun',
'an' : 'next word(s) is entity / noun',
'is' : 'assignment / equation ------ is = assignment moment == now & assignment ==True ',
'has' : 'assignment -> by becoming ---- was = assignment moment != now & assignment !=True now',
'to' : 'do next / causes next', # causes, in proximity of, --- the key to the upper cathedral, step closer to the choir, runs to fight
'of' : 'property / subset / part of',
'like' : 'previous statement applies to next',
'that' : 'statement about previous assigned entity',
'it' : 'statement about previous assigned entity',
'and' : 'combination',

'as' : 'indirect equation',
'within' : 'subset / part of - lesser version of "of"',
'while' : 'statement about previous comparison',
'like' : 'assignment to previous comparison',
'this' : 'assignment to previous previous comparison',

'which' : 'statement about previous assigned entity',
'into' : 'assignment -> by becoming',
'in' : 'part of',
'who' : 'assignment -> by becoming',
'was' : 'assignment -> by becoming ---- was = assignment moment != now & assignment !=True now',

'for' : 'assignment',
'with' : 'assignment',
'when' : 'assignment',
'why' : 'assignment',
'from' : 'assignment',
'by' : 'assignment',
'their' : 'assignment',
'they' : 'assignment',
'against' : 'assignment',
#------------------------------------

'if':'assignment',
'or':'assignment',
'but':'assignment',
'about':'assignment',
'out':'assignment',
'always':'assignment',
'never':'assignment',
'despite':'assignment',
'due':'assignment',
'then':'assignment',
'across':'assignment',
'among':'assignment',
'closest':'assignment',
'farthest':'assignment',
'though':'assignment',
'because':'assignment',
'perhaps':'assignment',
'maybe':'assignment',
'than':'assignment',
'too':'assignment',

'here':'assignment',
'there':'assignment',
'after':'assignment',
'before':'assignment',
'at':'assignment',
'since':' = now vs before --- implies states',
'later':'assignment',
'now':'assignment',
'sooner':'assignment',
'often':'assignment',
'anytime':'assignment',
'anywhere':'assignment',
'where':'assignment',
'what':'assignment',
'oldest':'assignment',
'available':'assignment'
}
funcWords = list(funcDict.keys()) 

verbEnds = ["ed","ing"] # do the overlapping words thins later, i.e. 'a gain' and 'to gain'
verbList = ["gain","are","become","have"]
numerical = ['one','two','three']

''' WORD AND LIST METHODS '''

''' 
-- TO DO --

- chain functions based on context
- hop between sentences
- be able to deal with verbs that do not have a noun before it 'create bofore the workshop existed' - thats just recognition
- establish context

make adjustments to clothing
to do
to use
to somewhere
to it

use to gain
runs to fight
key to the door
closer to the door
by allowing it
it allows
allows it
and is
'''

def evalFunc(func,sentence):
    """ check the surroundings of a func word to see if it changes the func context """
    # maybe even go back to the hierarchal evaluating of the text

def scanBack(char,indx,sentence):
    found = False
    for x in range(indx,0,-1):
        if str(sentence[x]).endswith(char):
            found = True
            break
    if found:
        return True
    else:
        return False

def scanForth(char,indx,sentence):
    found = False
    indx = 0
    for x in range(indx,len(sentence)):
        if str(sentence[x]).endswith(char):
            found = True
            indx = sentence[x+1]
            break
    if found:
        return indx
    else:
        return False

def scanThrough(word,sentence):
    # like 'one of the tools'
    if word in sentence.split(' '):
        return True
    else:
        return False



def splitSentence(txtIn,splitIndx):
    # break up sentences based on split indices; return a dict with 
    sentences = [[]]
    currIndx = []
    sentenceNr = 0
    split = False
    indx = 0
    for word in txtIn:
        # when cut is detected and the current word is not syntax; set to True
        if split == False and indx in splitIndx:
            split = True

        # special case; close and make new sentence at comma
        if split == False and ',' in word:
            split = False
            sentences[sentenceNr].append(word[:-1])
            sentenceNr += 1
            sentences.append([])
            currIndx.append(indx+1)

        # if True; set to False and make new sentence
        if split == True and indx in splitIndx:
            if indx+1 not in splitIndx:
                split = False
                sentenceNr += 1
                sentences.append([])
                currIndx.append(indx+1)

        # if no syntax and no new cut is detected; simply add word to current sentence
        if split == False and indx not in splitIndx:
            # special case addition
            if ',' not in word:
                sentences[sentenceNr].append(word)
        indx += 1

    if len(sentences[0]) == 0:
        del sentences[0]
    if len(sentences[0]) != 0:
        if len(sentences) > len(currIndx):
            currIndx.insert(0,0)

    out = {}
    incr = 0
    for x in sentences:
        #if ' '.join(x) != '':
        out[currIndx[incr]] = ' '.join(x)
        incr += 1

        if out[currIndx[incr-1]] == '':
            #print('DELETED incr = ' + str(incr) + ' in: ' + str(txtIn))
            del out[currIndx[incr-1]]
    return out


''' START DECONSTRUCTION '''

# test case
#'clawmark'
item = "molotov cocktail"
print('item = ' + item)

class Sentence():
    phrase = ''
    nr = 0
    assignments = []
    words = []

def nextWord(funcNr,sentence):
    if funcNr == len(sentence):
        return False
    else:
        return sentence[funcNr+1]

def isFunc(word,funcs):
    if word in funcs:
        return True
    return False


def hopForward(funcNr,hopper,entities,sentence):
    # use func[1], the index, to top to the next until non-func is found
    next = hopper[funcNr][1]
    
    if next not in entities.keys():
        return hopForward(next,hopper,entities,sentence)
    else:
        #print('outcome = ' + str(entities[next]))
        return entities[next]

def hopBack(funcNr,hopper,entities,sentence):
    # use func[1], the index, to hop to the next until non-func is found
    if funcNr == -1:
        return False

    prev = hopper[funcNr][0]
    if prev == -1:
        return False
    if hopper[prev][0] in entities.keys():
        return entities[hopper[prev][0]]


    #print('now = ' + str(funcNr) + ':' + str(hopper[funcNr]))
    #print('prev picked = ' + str(prev))
    if prev not in entities.keys():
        return hopBack(hopper[prev][0],hopper,entities,sentence)
    else:
        #print('outcome = ' + str(entities[prev]))
        return entities[prev]

def prevNonFunc(funcNr,hopper,sentence,funcList):
    if funcNr == -1:
        return False
    prev = sentence[hopper[funcNr][0]]
    if prev not in funcList:
        return prev
    return prevNonFunc(hopper[funcNr][0],hopper,sentence,funcList)
    

def nextNonFunc(funcNr,hopper,sentence,funcList):
    if funcNr == -1:
        return False
    next = sentence[hopper[funcNr][1]]
    if next not in funcList:
        return next
    return nextNonFunc(hopper[funcNr][1],hopper,sentence,funcList)

def scanForAssignment(sentence,assignFuncs):
    # look through a sentence for 'is','was','become', that kind of stuff
    assigns = []
    for x in sentence:
        if x in assignFuncs:
            assigns.append(x)

    if len(assigns) > 0:
        return assigns
    return False


        

sentenceDict = {}
for nr in range(len(phrases[item])):
    sen = Sentence()
    sen.phrase = phrases[item][nr]
    sentenceDict[nr] = sen
    
conclusions = []
for nr in range(len(sentenceDict)):
    phrase = sentenceDict[nr].phrase
    sentence = phrase.lower().split(' ')
    sentenceDict[nr].words = sentence

    idx = 0
    funcs = []
    funcIdx = []
    funcList = []

    endIdx = []
    verbs = []
    numbers = []
    # check the sentence for function words; list the index where found
    for word in sentence:
        if word in funcWords:
            funcs.append((word,idx))
            funcList.append(word)
            funcIdx.append(idx)
        if word in verbList:
            verbs.append((word,idx))
            funcIdx.append(idx)
        if word in numerical:
            numbers.append((word,idx))
            funcIdx.append(idx)

        """ REALLY CRUDE """
        if word[-2:] in verbEnds and word not in funcWords:
            verbs.append((word,idx))
            endIdx.append(idx)
        if word[-3:] in verbEnds and word not in funcWords:
            verbs.append((word,idx))
            endIdx.append(idx)

        idx += 1


    funcList = list(map(lambda x: x[0], funcs + verbs + numbers))
    
    print 'SCAN = ' + str(scanForAssignment(sentence,['is','become','have']))

    print(phrase.lower())
    print('sentence list = ' + str(sentence))
    print('<<>>')
    print('funcs = ' + str(funcs))
    print('verbs = ' + str(verbs))
    print('numbers = ' + str(numbers))
    entities = splitSentence(sentence,funcIdx + endIdx)
    print('entity splits = ' + str(entities))

    ''' check dependancy '''
    currentAssignment = [item,item]
    sentenceDict[nr].assignments.append((currentAssignment[0],0))
    sortedIdx = sorted(list(entities.keys()) + funcIdx)
    print('funcIdx = ' + str(funcIdx))
    print('sortedIdx = ' + str(sortedIdx))
    

    # lol; safeguard against sentences and phrases that have no split; due crappy sentence or lack of splits
    if len(sortedIdx) > 1:
        hopper = {}
        incr = 0
        # construct sentence hopper to allow easier jumping between func and normal words
        for x in sortedIdx:
            if incr == 0:
                hopper[x] = (-1,sortedIdx[incr+1])
            elif incr == len(sortedIdx)-1:
                hopper[x] = (sortedIdx[incr],-2)
            else:    
                hopper[x] = (sortedIdx[incr-1],sortedIdx[incr+1])
            incr += 1
        print('hopper -> ' + str(hopper))
        print('<<>>')

        for num in numbers:
            # eval functions and print result
            if num[0] == 'one':
                temp = hopBack(num[1],hopper,entities,sentence)
                if temp == False:
                    temp = currentAssignment[0]
                print ('one = ' + temp + ' <is> ' + hopForward(num[1],hopper,entities,sentence))
                print ('one = there are multiple ' + hopForward(num[1],hopper,entities,sentence))

        for verb in verbs:
            # eval functions and print result
            if verb[0] == 'have':
                print ('have = ' + hopBack(verb[1],hopper,entities,sentence) + ' <experience> ' + hopForward(verb[1],hopper,entities,sentence))

        for func in funcs:
            # eval functions and print result
            if func[0] == 'while':
                claim ='while = ' + entities[func[1]+1] + ' VS ' + currentAssignment[0]
                print (claim)
                conclusions.append(claim)

            if func[0] == 'against':
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]
                claim ='against = ' + currentAssignment[0] + ' VS ' + equals 
                print (claim)
                conclusions.append(claim)

            if func[0] == 'the':
                    claim ='the = ' + hopForward(num[1],hopper,entities,sentence)
                    print (claim)
                    conclusions.append(claim)

            if func[0] == 'a':
                    claim = 'a = ' + hopForward(num[1],hopper,entities,sentence)
                    print (claim)
                    conclusions.append(claim)

            ###########################################################################################################################################################################
            if func[0] == 'and':
                next = nextWord(func[1],sentence)
                if isFunc(next,funcList):
                    if next == 'is':
                        # 'and' becomes the previous assignment
                        claim ='and = ' + currentAssignment[0]  + ' \'is\' ' + nextNonFunc(func[1],hopper,sentence,funcList)
                        print (claim)
                        conclusions.append(claim)
                else:
                    claim ='and = ' + prevNonFunc(func[1],hopper,sentence,funcList) + ' + ' + nextNonFunc(func[1],hopper,sentence,funcList)
                    print (claim)
                    conclusions.append(claim)

            if func[0] == 'an':
                claim ='an = ' + entities[func[1]+1]
                print (claim)
                conclusions.append(claim)

            if func[0] == 'this':
                claim ='this -> ' + currentAssignment[0] + ' = ' + hopForward(func[1],hopper,entities,sentence)
                print (claim)
                conclusions.append(claim)

            if func[0] == 'it':
                claim ='it = ' + currentAssignment[0]
                #print ('it -> ' + currentAssignment[0] + ' = ' + entities[func[1]+1]) # is this correct or still needed?
                print (claim)
                conclusions.append(claim)

            if func[0] == 'who':
                claim ='who = ' + entities[hopper[func[1]][0]]
                print (claim)
                conclusions.append(claim)

            if func[0] == 'that':
                claim ='that -> ' + currentAssignment[0] + ' = ' + entities[hopper[func[1]][0]]
                print (claim)
                conclusions.append(claim)
                claim ='that -> ' + entities[hopper[func[1]][0]] + ' = ' + entities[hopper[func[1]][1]]
                print (claim)
                conclusions.append(claim)

            if func[0] == 'which':
                claim ='which -> ' + currentAssignment[1] + ' = ' + hopForward(func[1],hopper,entities,sentence)#entities[hopper[func[1]][1]])
                print (claim)
                conclusions.append(claim)

            if func[0] == 'is':
                if func[1] > 1:
                    currentAssignment[0] = hopBack(func[1],hopper,entities,sentence)#entities[hopper[func[1]][0]]
                    # record assignment
                    #if (entities[hopper[func[1]][0]],len(sentenceDict[nr].assignments)) not in sentenceDict[nr].assignments:
                    #    sentenceDict[nr].assignments.append((entities[hopper[func[1]][0]],len(sentenceDict[nr].assignments)))

                equals = hopForward(func[1],hopper,entities,sentence)#entities[hopper[func[1]][1]]

                currentAssignment[1] = equals

                claim = 'is -> ' + currentAssignment[0] + ' = ' + equals
                print (claim)
                conclusions.append(claim)

            if func[0] == 'has':
                if func[1] > 1:
                    currentAssignment[0] = prevNonFunc(func[1],hopper,sentence,funcList)#entities[hopper[func[1]][0]]
                    # record assignment
                    #if (entities[hopper[func[1]][0]],len(sentenceDict[nr].assignments)) not in sentenceDict[nr].assignments:
                    #    sentenceDict[nr].assignments.append((entities[hopper[func[1]][0]],len(sentenceDict[nr].assignments)))

                equals = nextNonFunc(func[1],hopper,sentence,funcList)#entities[hopper[func[1]][1]]

                currentAssignment[1] = equals

                claim ='has -> ' + currentAssignment[0] + ' = now -> ' + equals
                print (claim)
                conclusions.append(claim)
                claim ='has -> ' + currentAssignment[0] + ' was not before: ' + equals
                print (claim)
                conclusions.append(claim)

            if func[0] == 'since':
                equals = hopForward(func[1],hopper,entities,sentence)
                go = scanForth(',',func[1],sentence)
                
                claim = 'since -> ' + go + ' =now ' + equals
                print (claim)
                conclusions.append(claim)

            if func[0] == 'when':
                equals = hopForward(func[1],hopper,entities,sentence)#entities[hopper[func[1]][1]]
                claim ='when -> ' + currentAssignment[0] + ' <is> ' + equals
                print (claim)
                conclusions.append(claim)


            if func[0] == 'their':
                if func[1] > 1:
                    try:
                        temp = entities[hopper[func[1]][0]]
                    except KeyError:
                        temp = entities[hopper[hopper[func[1]][0]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]
                currentAssignment[1] = equals

                claim ='their = ' + currentAssignment[0] + '\'s= ' + equals
                print (claim)
                conclusions.append(claim)
                #print ('their -> ' + temp + ' => ' + equals) # goes back to 'they', that in turn goes back to 'hunters'


            if func[0] == 'was':
                if func[1] > 1:
                    try:
                        currentAssignment[0] = entities[hopper[func[1]][0]]
                    except KeyError:
                        pass #currentAssignment[0] = currentAssignment[0]

                equals = hopForward(func[1],hopper,entities,sentence)

                currentAssignment[1] = equals

                claim ='was -> ' + currentAssignment[0] + ' <= ' + equals
                print (claim)
                conclusions.append(claim)
            

            if func[0] == 'as':
                if func[1] > 1:
                    currentAssignment[0] = entities[hopper[func[1]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]
                currentAssignment[1] = equals
                if currentAssignment[0] == '':
                    claim ='as -> ' + 'statement about = ' + equals
                    print (claim)
                    conclusions.append(claim)
                else: 
                    claim ='as -> ' + currentAssignment[0] + ' = ' + equals
                    print (claim)
                    conclusions.append(claim)

            if func[0] == 'into':
                if func[1] > 1:
                    #currentAssignment[0] = entities[hopper[func[1]][0]]
                    pass
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]
                currentAssignment[1] = equals

                claim  ='into -> ' + currentAssignment[0] + ' => ' + equals
                print (claim)
                conclusions.append(claim)


            if func[0] == 'within':
                temp = ''
                if func[1] > 1:
                    temp = entities[hopper[func[1]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]

                print ('within -> ' + temp + ' <in> ' + equals)


            if func[0] == 'of':
                temp = ''
                if func[1] > 1:
                    
                    temp = hopBack(func[1],hopper,entities,sentence)
                elif func[1] == 1:
                    temp = hopBack(func[1],hopper,entities,sentence)
                    #temp = entities[hopper[func[1]][0]]
                    if not temp:
                         temp = currentAssignment[0]
                try:
                    equals = hopForward(func[1],hopper,entities,sentence)

                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]

                print ('of -> ' + equals + '_' + temp) # lol; abnormal fear of flame -> flame's abnormal fear
                #print ('of -> ' + equals + '\'s ' + temp) # note: not as simple as 's

            if func[0] == 'from':
                temp = ''
                if func[1] > 1:
                    temp = entities[hopper[func[1]][0]]
                elif func[1] == 1:
                    temp = entities[hopper[func[1]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]

                print ('from -> ' + equals + '_' + temp)


            if func[0] == 'in':
                temp = ''
                if func[1] > 1:
                    temp = hopBack(func[1],hopper,entities,sentence)#entities[hopper[func[1]][0]]
                elif func[1] == 1:
                    temp = hopBack(func[1],hopper,entities,sentence)

                equals = hopForward(func[1],hopper,entities,sentence)
                print ('in -> ' + equals + '\'s ' + temp) # lol; adrift = status

            if func[0] == 'by':
                temp = ''
                if func[1] > 1:
                    temp = entities[hopper[func[1]][0]]
                elif func[1] == 1:
                    temp = entities[hopper[func[1]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]

                print ('by -> ' + temp + ' <using> ' + equals) # using

            if func[0] == 'like':
                temp = ''
                if func[1] > 1:
                    temp = entities[hopper[func[1]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]

                print ('like -> ' + equals + ' = ' + currentAssignment[0])

            if func[0] == 'for':
                temp = ''
                if func[1] > 1:
                    temp = entities[hopper[func[1]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]

                print ('for -> ' + equals + ' = ' + currentAssignment[0]) # reverence, for their victims; really need a way to hop back multiple assignments or lines

            if func[0] == 'with':
                temp = ''
                if func[1] > 1:
                    temp = entities[hopper[func[1]][0]]

                equals = hopForward(func[1],hopper,entities,sentence)


                print ('with -> ' + temp + '_' + equals)


            if func[0] == 'to':
                temp = ''
                if func[1] > 1:
                    temp = entities[hopper[func[1]][0]]
                try:
                    equals = entities[hopper[func[1]][1]]
                except KeyError:
                    equals = entities[hopper[func[1]][1]+1]

                # if 'to' = the first word, switch sentences
                print ('to -> ' + currentAssignment[1] + ' <causes> ' + equals)

            if func[0] == 'they':
                if func[1] == 0:
                    currentAssignment[0] = func[0]
                    # go back to previous sentence
                    print ('they -> ' + sentenceDict[nr-1].words[0])
            
            if func[0] == 'oldest':
                print ('oldest ->  there are old and new ' + equals)

            if func[0] == 'available':
                print ('available -> '+ hopBack(func[1],hopper,entities,sentence) +' = available @ ' + hopForward(func[1],hopper,entities,sentence))
            
            

    #print(str(sentenceDict[nr].assignments))
    print('---------------------------')

print('CONCLUSIONS')
for x in conclusions:
    print(x)

""" DERIVATIVES """

'''
Molotov Cocktail
explodes in raging flames when thrown against an object
one of the oldest hunter tools available in the workshop
since the tragedy that struck old yharnam, fire has become a staple in beast hunts, and is thought to cleanse impurity
certain types of beasts have an abnormal fear of flame

Motolov explodes when thrown against object
Molotov can be thrown
Motolov causes fire
Motolov can explodes

Motolov is a tool
Motolov is a tool in the workshop
there are old and new tools
tools are available in the workshop
hunters use tools
there are multiple tools

throwing is a condition
objects can be thrown against
there are multiple objects


the tragedy struck Old yharnam
it was a signitifacnt tragedy, due to 'the'
tragedy involved fire
before tragedy, fire was not a staple in beast hunts
beasts are hunted
fire is used in beast hunts
fire is thought to cleanse impurity

flames are fire
there are multiple types of beasts
some beast fear fire
the fear is abnormal

# when = condition, so implies 'can', not 'must'
# one of the 


though (echter) = i.e. I thought it was right, but it turned out not to be. 'That statement is not correct though' = an interjection to a previous statement
before actual check, one evalled the check to true based on presumed condition, but after check it is not (probably because conditions were not real)


'''
