#!/usr/bin/python

import collections, itertools
#from n_gram_iterators import *

class Brain:
  def __init__(self,corpus):
    '''
    Populate training data into memory.

    @param:
      name of file containg n-gram data(+ tweets)
    @return:
      list() of tuples
      ex: [("spoiled","-1,...") ,("unpredicatable", "movie", "1,...")]
        last element of tuple is a comma seperated string mapping ("",..., "<polarity>, ...")
    '''
    f = open(corpus)
    b = []
    #iterate over file to populate n_grams into brain
    while True:
      line = f.readline()
      if not line: break
      #omit comments and newlines
      if line[0] != '#' and line != '\n':
        #line is a list now
        line = line.strip().split(',')
        b.append(tuple(line))
    self.data = b

  def has_key(self, key):
    #key here is a tuple of words
    pass

  def polarity(self, ngram):
    '''
    Analyse corpus and return a polarity matching the give ngram.

    @param:
      tuple()
    @return:
      int -1, 0 or 1
    '''
    for knowledge in self.data:
      #here knowlede is a tuple
      #print set(ngram), set(knowledge[0:-1]), '=>',knowledge[-1],'\n' 
      if ( set(ngram) == set(knowledge[0:-1]) )  :
        #strip polarity away and make sets so order doen not matter
        #print set(ngram), set(knowledge[0:-1]), '=>',knowledge[-1],'\n'
        return int(knowledge[-1])
    return 0

def sentence_gram(raw_sentence):
  '''
  N-gram(ize) a sentence and try matching with corpus.
  //currently, we do 1,2 & 3-gram

  @param:
    raw sentence
  @return:
    list of tuples
  '''
  sg = list()
  w_list = raw_sentence.split(' ')
  for i in range(1,3):
    sg += list(itertools.permutations(w_list, i))
  return sg

def analyse(sentence=None, corpus='corpus.txt'):
  if not sentence: sentence = raw_input(">")
  sg = sentence_gram( sentence )
  brain = Brain(corpus)
  polarity = 0
  print '\n\n'
  for ngram in sg:
    #here ngram is a tuple of 1,2 or 3 gram
    polarity += brain.polarity(ngram)
    #print ngram, brain.polarity(ngram), '\n'

  return polarity
  	

if __name__ == "__main__":
  #print Brain("corpus.txt").polarity(("made",))
  #print sentence_gram("the mp3 is unpredicatable")
  while(1):
    print analyse()
