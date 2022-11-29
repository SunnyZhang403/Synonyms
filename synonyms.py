'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math
import re

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)
def dotprod(vec1, vec2):
    dotprod = 0
    for n in vec1:
        if n in vec2:
            dotprod = dotprod + vec1[n]*vec2[n]
    return dotprod

def cosine_similarity(vec1, vec2):
    return dotprod(vec1,vec2)/(norm(vec1)*norm(vec2))
# print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
def build_semantic_descriptors(sentences):
    words = {}
    for i in range (len(sentences)):
        for curword in sentences[i]:
            curworddict = {}
            if len(curword) ==None:
                continue
            if curword not in words and len(curword) >= 1:
                words[curword] = {}
            for k in sentences[i]:
                if k != curword:
                    if k not in curworddict:
                        curworddict[k] = 1
                    else:
                        curworddict[k] = curworddict[k] +1
            for m in curworddict:
                if len(m) < 0:
                    continue
                if m not in words[curword]:
                    words[curword][m] = curworddict[m]
                else:
                    words[curword][m] = words[curword][m] + curworddict[m]


    return words

# print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
# ["i", "am", "a", "spiteful", "man"],
# ["i", "am", "an", "unattractive", "man"],
# ["i", "believe", "my", "liver", "is", "diseased"],
# ["however", "i", "know", "nothing", "at", "all", "about", "my",
# "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))

def build_semantic_descriptors_from_files(filenames):
    punc = [",", "-","--", ":", ";"]
    allwords = []
    for i in range(len(filenames)):

        curname = "D:\\Laptop Archive\\Sunny\\School Work\\UofT 2022-2023\\ESC180\\projects\\%s" %filenames[i]
        curfile = open(curname)
        text = curfile.read()
        sentences = re.split('\? |\! |\. |\.|\?|\!', text)
        for j in range (len(sentences)):
            modsentence = re.sub("\,|\-|\:|\;|", "", sentences[j])

            words = modsentence.split(" ")
            allwords.append(words)

    desc = build_semantic_descriptors(allwords)

    return desc
# print(build_semantic_descriptors_from_files(["mickeymouse.txt","mickeymouse2.txt"]))



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    scores = {}
    for choice in choices:
        if choice not in semantic_descriptors:
            scores[choice] = -1
        else:
            scores[choice] = cosine_similarity(semantic_descriptors[word], semantic_descriptors[choice])
    return max(scores)
most_similar_word("i", ["to", "am"], build_semantic_descriptors_from_files(["mickeymouse.txt"]), cosine_similarity)
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    curname = "D:\\Laptop Archive\\Sunny\\School Work\\UofT 2022-2023\\ESC180\\projects\\%s"%filename
    curfile = open(curname)
    text = curfile.read()
    curscore =0
    for l in text.split("\n"):
        store = l.split(' ')
        word = store[0]
        coranswer = store[1]
        choices = store[2:]
        if most_similar_word(word,choices,semantic_descriptors, cosine_similarity) == coranswer:
            curscore = curscore+1
    return curscore/len(text.split("\n"))*100
