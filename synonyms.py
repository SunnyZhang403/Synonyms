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

def build_semantic_descriptors(sentences):
    words = {}
    for sentence in sentences:
        for curword in sentence:
            if curword == "":
                    continue
            if curword not in words:
                words[curword] = {}
            for k in sentence:
                if k != curword:
                    if k not in words[curword]:
                        words[curword][k] = 1
                    else:
                        words[curword][k] = words[curword][k] + 1

    return words

def build_semantic_descriptors_from_files(filenames):
    punc = [",", "-","--", ":", ";"]
    allwords = []
    for i in range(len(filenames)):

        curfile = open(filenames[i], encoding = "latin1")
        text = curfile.read()
        sentences = re.split('\? |\! |\. |\.|\?|\!', text)
        for j in range (len(sentences)):
            lowsentence = sentences[j].lower()
            modsentence1 = re.sub("\,|\:|\;|", "", lowsentence)
            modsentence2 = re.sub("\-|\n", " ",modsentence1)


            words = modsentence2.split(" ")
            allwords.append(words)

    desc = build_semantic_descriptors(allwords)

    return desc



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    scores = {}
    for choice in choices:
        if choice not in semantic_descriptors:
            scores[choice] = -1
        else:
            scores[choice] = cosine_similarity(semantic_descriptors[word], semantic_descriptors[choice])
    wordscores = list(scores.values())
    words = list(scores.keys())


    return words[wordscores.index(max(wordscores))]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):


    curfile = open(filename)
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


