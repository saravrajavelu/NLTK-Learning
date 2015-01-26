from nltk.corpus import names
import nltk
import random

labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)


def fun(string):
	m = 0
	f = 0
	for name in labeled_names:
		if(name[0].endswith(string)):
			print(name[0])
			if(name[1] == 'male'):
				m +=1
			elif(name[1] == 'female'):
				f +=1
	print("Male : Female :: ",m, " : " ,f)




def gender_features2(name):
    features = {}

    '''
    features["firstletterVowel"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    '''

    if name[0].lower() in 'aeiou':
        features["firstletterVowel"] = 1
        features["firstletterConsonant"] = 0
    else:
        features["firstletterVowel"] = 0
        features["firstletterConsonant"] = 1

    if name[-1].lower() in 'aeiou':
        features["lastletterVowel"] = 1
        features["lastletterConsonant"] = 0
    else:
        features["lastletterVowel"] = 0
        features["lastletterConsonant"] = 1 


    '''Trigrams ['ric', 'art', 'har', 'ton', 'ard', 'ber', 'ina', 'ine', 'lin', 'nne', 'ett', 'nna', 'ari', 'ann', 'lla', 'eli', 'ris', 'lyn', 'rie', 'lle'] '''    
    features["countVowels"] = name.lower().count('a') + name.lower().count('e') + name.lower().count('i') + name.lower().count('o') + name.lower().count('u')
    features["nameLength"] = len(name)
    features["countConsonants"] = features["nameLength"] - features["countVowels"]
    
    return features

featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(10))
tempInput = input("Enter a name : ")

print(classifier.classify(gender_features2(tempInput)))
