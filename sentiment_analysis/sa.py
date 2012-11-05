#!/usr/bin/python

import collections

def n_gram_data(file):
  '''
  Populate n-gram data into memory.

  @param:
    name of file containg n-gram data
  @return:
    dict() with key as n-gram and value as a list.
    ex: {"spoiled" : [-1,...], "unpredicatable movie":[1,...]}
      first element of list is polarity : maybe -1, 1, 0
  '''
  f = open(file)
  n_gram = {}
  #iterate over file to populate n_grams
  while True:
    line = f.readline()
    if not line: break
    if line[0] != '#' and line != '\n':
      #line is a list now
      line = line.strip().split(',')
      n_gram[line[0]] = line[1]

def sentence(raw):
  '''
    
  '''

if __name__ == "__main__":
  n_gram_data("n_gram.data")
