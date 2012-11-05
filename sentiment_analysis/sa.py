#!/usr/bin/python

import collections

def train(corpus):
  '''
  Populate training data into memory.

  @param:
    name of file containg n-gram data(+ tweets)
  @return:
    dict()
    ex: {"spoiled":"-1,...","unpredicatable movie":"1,..."}
      first element of tuple is n-gram entity
      next is polarity : maybe -1, 1, 0
  '''
  f = open(corpus)
  n_gram = {}
  #iterate over file to populate n_grams
  while True:
    line = f.readline()
    if not line: break
    #omit comments and spaces
    if line[0] != '#' and line != '\n':
      #line is a list now
      line = line.strip().split(',')
      n_gram[line[0]]=line[1]
  return n_gram

def sentence_gram(raw_sentence):
  '''
  N-gram(ize) a sentence and try matching with corpus.

  @param:
    raw sentence
  @return:
    collections.Counter object, containg occurence of 
    >3 letter word in raw_sentence. This insures that 
    and, is, to, etc. are ignored.
  '''
  cnt = collections.Counter()
  w_list = raw_sentence.split(' ')
  for word in w_list:
    if len(word)>3:
      #1 gram
      cnt[word] += 1

    #2 gram
    try:
      cnt[word + ' ' + w_list[ w_list.index(word) + 1] ] += 1
    except IndexError, e:
      pass

  return cnt

def analyse(sentence=None):
  if not sentence: sentence = raw_input(">")
  sg = sentence_gram( sentence )
  brain = train('n_gram.txt')
  polarity = 0
  for word in sg:
    if brain.has_key(word):
      polarity += brain[word]
  return polarity
  	

if __name__ == "__main__":
  print train("n_gram.txt")
  print sentence_gram("to infinity and beyond")
