import nltk
from nltk.corpus import names
from nltk.collocations import *
from nltk import bigrams
from nltk import trigrams
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

maleNames = ((name) for name in names.words('male.txt'))
femaleNames = ((name) for name in names.words('female.txt'))


def bigramGenerator(listOfNames):
    bigramFreqDist = []
    wordFreqDist = []
    for name in listOfNames:
        bigramFreqDist += list(bigrams(list(name.lower())))
        wordFreqDist += list(name.lower())

    wordFreqDist = nltk.FreqDist(wordFreqDist)
    bigramFreqDist = nltk.FreqDist(bigramFreqDist)
    finder = BigramCollocationFinder(wordFreqDist, bigramFreqDist)
    scored = finder.score_ngrams(bigram_measures.raw_freq)
    return (sorted(bigram for bigram, score in scored)[1:10] )


def trigramGenerator(listOfNames):
    trigramFreqDist = []
    bigramFreqDist = []
    wordFreqDist = []
    for name in listOfNames:
        trigramFreqDist += list(trigrams(list(name.lower())))
        bigramFreqDist += list(bigrams(list(name.lower())))
        wordFreqDist += list(name.lower())

    wildcard = [ w for w in set(wordFreqDist) if w not in ".-/_#!@$%^&*()\'\"\\"]
    
    wildcardFreqDist = nltk.FreqDist(wildcard)
    wordFreqDist = nltk.FreqDist(wordFreqDist)
    bigramFreqDist = nltk.FreqDist(bigramFreqDist)
    trigramFreqDist = nltk.FreqDist(trigramFreqDist)
    finder = TrigramCollocationFinder(wordFreqDist,bigramFreqDist,wildcardFreqDist, trigramFreqDist)
    scored = finder.score_ngrams(trigram_measures.raw_freq)
    return (sorted(trigram for trigram, score in scored)[1:10] )


def altTrigramGenerator(listOfNames):
    trigram = []
    for name in listOfNames:
        trigram += list(trigrams(list(name.lower())))

    trigramFreqDist = nltk.FreqDist(trigram)
    mostCommon = trigramFreqDist.most_common(10)
    for eachGram in mostCommon:
        tempGram = eachGram[0][0]+eachGram[0][1]+eachGram[0][2]
        print(tempGram,"  ",eachGram[1])
    

    
print('----------------------------------')
print('Male')
altTrigramGenerator(maleNames)
print('----------------------------------')
print('----------------------------------')
print('Female')
altTrigramGenerator(femaleNames)
    
