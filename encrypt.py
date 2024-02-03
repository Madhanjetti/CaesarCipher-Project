LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(initial, shift):
  """ Use : encrypt('virat', 1)
  => 'gymmuay'
  
  Encrypts text using Caesar Cipher
  """
  initial = initial.lower()
  output = ""

  for char in initial:
    if char in LETTERS:
      output += LETTERS[(LETTERS.index(char) + shift) % len(LETTERS)]

  return output
print(encrypt('virat', 1))