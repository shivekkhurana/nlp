from spell_check import *
def main():
  a = Spelling("acress")
  print a.correct()

  a = Spelling("coumpter")
  print a.correct()
  from os import remove
  remove("spell_check.pyc")

if __name__ == "__main__":
  main()
