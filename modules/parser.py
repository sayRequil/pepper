# Parsing module~~ Pepper 1.0
from sys import *

filename = argv[1]

def open_file(file):
  data = open(filename + ".pep","r").read()
  return data
  
def lex(filecontents):
  filecontents = list(filecontents)
  tok = ""
  state = 0
  string = ""
  tokens = []
  for char in filecontents:
    tok += char
    if tok == " ":
      if state == 0:
        tok = ""
      else:
        tok = " "
    elif tok == "\n":
        tok = ""
    elif tok == "print":
      tokens.append("PRINT")
      tok = ""
    elif tok == "\"":
      if state == 0:
        state = 1
      elif state == 1:
        tokens.append("STRING:" + string)
        state = 0
        string = ""
        tok = ""
    elif state == 1:
      string += tok
      tok = ""
  return tokens
  
def parse(toks):
  i = 0
  while i < len(toks):
    if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
      print(toks[i+1][7:])
      i += 2
  
def run():
  open_file(filename)
  toks = lex(data)
  parse(toks)
