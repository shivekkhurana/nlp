class Spelling:
  def __init__(self, obs):
    """
      Create a spelling observation for processing.
      NOISY CHANNEL ALGORITIHM with step 2 modified.
    """
    self.obs  = obs
    self.size = len(obs)

    #for regex matching
    self.alphabets = "[a-z]"
    self.alpha_a = "[a-z']" #alphabets including apostrophe

    #imports 
    import re
    return None

  def candidate_set(self):
    """
    Genrate a list of candidate set using the noisy
    channel step 1 fact that each spelling mistake can
    be corrected by making just one insertion, deletion,
    substitution or transposition.

    ALGORITHM
    =========
    Given an observation, say 'abck', an Insertion can be
    made at n+1 positions. [a-z]abck, a[a-z]bck, ..., abck[a-z]
    Substituition can be made in n ways. [a-zbck], ...
    Deletion in n ways
    Transposition in n ways
    Use regex to match everything

    @param None
    @return dict with each key mapping to 0
    """
    obs = list(self.obs)
    size = self.size
    regexes = []

    #iterate over list and generate regexes
    i,j = 0,0
    while(i<=size):
      temp = '' #an empty string to populate regex
      while(j<i):
        temp += obs[j]
        j+=1

      temp += self.alphabets

      while(j < size):
        temp += obs[j]
        j+=1
      regexes.append(temp)
      i+=1
      j=0

    return regexes

  def edit_distance(self):
    """
      Calc. Demaro Levenstein edit distance between obs. and candidate set
    """
    pass

