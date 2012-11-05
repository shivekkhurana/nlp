#!/usr/bin/python

import collections

def train(corpus):
  '''
  Populate training data into memory.

  @param:
    name of file containg n-gram data(+ tweets)
  @return:
    list() of tuples
    ex: [("spoiled",-1,...), ("unpredicatable movie",1,...)]
      first element of tuple is n-gram entity
      next is polarity : maybe -1, 1, 0
  '''
  f = open(corpus)
  n_gram = []
  #iterate over file to populate n_grams
  while True:
    line = f.readline()
    if not line: break
    if line[0] != '#' and line != '\n':
      #line is a list now
      line = line.strip().split(',')
      n_gram.append( (line[0], line[1]) )
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

if __name__ == "__main__":
  print train("n_gram.txt")
  print sentence_gram("to infinity and beyond")
