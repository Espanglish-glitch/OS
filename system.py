from math import sqrt
print(sqrt(16))

#AN OS
print("AN", " OS")

class Token():
  def __init__(self, contents:str, type):
    self.val = contents
    self.type = type
  

def lex(string:str):
  i = 0
  while i < len(string):
    if character.isspace():
      i += 1
      continue
    elif character.isalpha()
      I = 0
      interestIndex = i
      while character.isalnum() or character == "_" or character == "-":
        i += 1
        continue
      yield Token(string[interestIndex:i], "identifier)
