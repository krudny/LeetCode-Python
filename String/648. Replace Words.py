# In English, we have a concept called root, which can be followed by some other word to form another longer word 
# - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
# replace all the derivatives in the sentence with the root forming it. 
# If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"

def replaceWords(dictionary, sentence):
    sentence = sentence.split(' ')
    dictionary = set(dictionary)

    for i, word in enumerate(sentence): 
        for j in range(len(word)): 
            if word[0:j+1] in dictionary: 
                sentence[i] = word[0:j+1]
                break

    sentence = ' '.join(sentence)
    return sentence

print(replaceWords(dictionary, sentence))