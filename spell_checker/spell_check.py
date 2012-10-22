class Spelling:
  def __init__(self, obs):
    """
      Create a spelling observation for processing
    """
    self.obs  = obs
    self.size = len(obs)
    return None

    def candidate_set(self):
      pass
      #return dict with each key mapping to 0

    def edit_distance(self):
      """
        Calc. Demaro Levenstein edit distance between obs. and candidate set
      """
      pass

