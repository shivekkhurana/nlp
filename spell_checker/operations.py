#!/usr/bin/env/python
"""
  Common operations used by spell_check.py
"""

def insert(string, position, insert):
  """
  Usage:
    insert("hello", 1, "x")
    returns "hxello"

    insert("hello", 0, "xy")
    returns "xyhello"
  """
  #fix types
  (string, position, insert) = (str(string), int(position), str(insert))
  size = len(string)
  if(position < 0 or position > size+1):
    raise Exception("Expected position >=0 %s given"%position)
  return string[0:position] + insert + string[position:size]

def sub(string, position, sub):
  """
  position of sub. is zero based
  Usage:
    sub("hello", 0, "a")
    return "aello"
  """
  #fix types
  (string, position, sub) = (str(string), int(position), str(sub))
  size = len(string)
  if(position<0 or position>size):
    raise Exception("Expected position >=0 and position < size %s given"%position)
  return string[0:position] + sub + string[position+1:size]

def delete(string, position):
  """
  position is zero based
  Usage:
    delete("hello",0)
    return "ello"
  """
  #fix types
  (string, position) = (str(string), int(position))
  size = len(string)
  if(position<0 or position>size):
    raise Exception("Expected position >=0 and position < size %s given"%position)
  return string[0:position] + string[position+1:size]

def all_trans(string):
  """
  Get all transpositions in a list.
  Usage all_trans("abck")
  return ["back", "acbk", "abkc"]
  """
  size = len(string)
  trans = []
  for i in range(0, size-1):
    temp = string
    temp = list(temp)
    temp2 = temp[i+1]
    temp[i+1] = temp[i]
    temp[i] = temp2
    trans.append("".join(temp))
  return trans

def main():
  print all_trans("hello")

if __name__ == "__main__":
  main()
