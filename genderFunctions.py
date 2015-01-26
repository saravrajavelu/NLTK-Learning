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


def altBigramGenerator(listOfNames):
    bigram = []
    outputList = []
    namesLength = 0
    for name in listOfNames:
        bigram += list(bigrams(list(name.lower())))
        namesLength += 1

    bigramFreqDist = nltk.FreqDist(bigram)
    mostCommon = bigramFreqDist.most_common(50)
    print("No of names in this category : ",namesLength)
    for eachGram in mostCommon:
        tempGram = eachGram[0][0]+eachGram[0][1]
        outputList.append(tempGram)
        print(tempGram,"  Percentage Occurance : ",(int(eachGram[1])/namesLength))
    return (outputList)


def altTrigramGenerator(listOfNames,threshold):
    trigram = []
    namesLength = 0
    outputList = []
    for name in listOfNames:
        trigram += list(trigrams(list(name.lower())))
        namesLength += 1

    trigramFreqDist = nltk.FreqDist(trigram)
    mostCommon = trigramFreqDist.most_common(50)
    print("No of names in this category : ",namesLength)
    for eachGram in mostCommon:
        tempGram = eachGram[0][0]+eachGram[0][1]+eachGram[0][2]
        percentageOccurance = int(eachGram[1])/namesLength
        if threshold < percentageOccurance:
            outputList.append(tempGram)
        print(tempGram,"  Percentage Occurance : ",percentageOccurance)
    return (outputList)

def trigramList(maleNames,femaleNames,threshold):
    print('Male Trigrams')
    maleTrigrams = altTrigramGenerator(maleNames,threshold)
    print('Female Trigrams')
    femaleTrigrams = altTrigramGenerator(femaleNames,threshold)

    print('Male Trigrams Passing Threshold')
    print(maleTrigrams)
    print('Female Trigrams Passing Threshold')
    print(femaleTrigrams)
    
    allTrigrams = list(set(maleTrigrams) - (set(maleTrigrams) & set(femaleTrigrams))) + list(set(femaleTrigrams) - (set(maleTrigrams) & set(femaleTrigrams)))
    print(allTrigrams)
    return(allTrigrams)
    
    
    
'''
print('----------------------------------')
print('Male')
altTrigramGenerator(maleNames)
print('----------------------------------')
print('----------------------------------')
print('Female')
altTrigramGenerator(femaleNames)
'''    
