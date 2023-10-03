import urllib.request,sys,os
import operator,os,re,sys,inspect # default imports
import sqlite3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from gwentData import *




def vizKeywords():
    ''' DRAAWWWWWWWW '''

    word_groups = len(allKeywords)
    fig, ax = plt.subplots(figsize=(word_groups * 2.0,  10))
    print(word_groups)  # 117
    index = np.arange(word_groups)
    bar_width = 0.1
    opacity = 0.7

    error_config = {'ecolor': '0.3'}

    clrs = ['k', 'm', 'b', 'g', 'r', 'c', 'y']  # 'w' m

    incr = 0
    for house in list(Factions):

        testWords = [house.uniquekeyWords()[word] if word in house.uniquekeyWords() else 0 for word in allKeywords]

        houseWords = tuple(testWords)#[:40]
        # houseWords = tuple(house.uniquekeyWords().values())#[:40]

        ax.bar(index + (bar_width*(incr+1))-(bar_width* 3.5), houseWords, bar_width,
                        alpha=opacity, color=clrs[incr], error_kw=error_config, label= house.name)

        incr += 1


    ax.set_xlabel('words')
    ax.set_ylabel('freq')
    # ax.set_title('Scores by group and gender')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(tuple(allKeywords))
    ax.legend()
    ax.axhline(10, color='grey', alpha=0.25)
    ax.axhline(1, color='grey', alpha=0.25)

    #fig.tight_layout()
    plt.savefig(r'C:\Users\rober\Google Drive\Games\Gwent\wordFreq.png')

    plt.show()

# vizKeywords()






def radialKeywords():
    ''' DRAAWWWWWWWW '''

    word_groups = len(allKeywords)
    # fig, ax = plt.subplots(figsize=(word_groups * 2.0,  10))
    # print(word_groups)  # 117
    index = np.arange(10)
    bar_width = 0.1
    # opacity = 0.7

    error_config = {'ecolor': '0.3'}

    clrs = ['k', 'm', 'b', 'g', 'r', 'c', 'y']  # 'w' m

    # incr = 0
    # for house in list(loadedFactions):
    #
    #     testWords = [house.uniquekeyWords()[word] if word in house.uniquekeyWords() else 0 for word in allKeywords]
    #
    #     houseWords = tuple(testWords)#[:40]
    #     # houseWords = tuple(house.uniquekeyWords().values())#[:40]
    #
    #     ax.bar(index + (bar_width*(incr+1))-(bar_width* 3.5), houseWords, bar_width,
    #                     alpha=opacity, color=clrs[incr], error_kw=error_config, label= house.name)
    #
    #     incr += 1

    testWords = [float(Factions[0].uniquekeyWords()[word]) if word in Factions[0].uniquekeyWords() else 0 for word in allKeywords]
    intWords = [Factions[0].uniquekeyWords()[word] if word in Factions[0].uniquekeyWords() else 0 for word in allKeywords]
    print(testWords)
    #plz = np.arange(testWords)

    # ax.axhline(10, color='grey', alpha=0.25)
    # ax.axhline(1, color='grey', alpha=0.25)

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    lol = np.array(testWords)
    kek = np.array(intWords)


    # Compute pie slices
    N = len(testWords)
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 12 #* np.random.rand(N)
    colors = plt.cm.viridis(radii / 10.)

    ax = plt.subplot(111, projection='polar')
    ax.bar(theta, testWords, width=width, bottom=0.0, color=colors, alpha=0.5)

    ax.set_xlabel('words')
    ax.set_ylabel('freq')
    ax.set_title('Scores by group and gender')

    ax.set_xticks(np.arange(117))# + bar_width / 2)
    ax.set_xticklabels(tuple(allKeywords))

    #ax.legend()

    # fig.tight_layout()
    # plt.savefig(r'C:\Users\rober\Google Drive\Games\Gwent\wordFreq.png')

    plt.show()

