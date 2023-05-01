import sys 

def caesar_cipher(shift, plaintext):
  ciphertext = ""
  row = column = 1
  for char in plaintext.upper():    
    if char.isalpha() == True:
      asc_char = ord(char)
      new_char_code = asc_char + shift
      if new_char_code > 90:
        remaining = new_char_code - 90
        new_char_code = 64 + remaining
      new_char = chr(new_char_code)
      if row == 5:
        ciphertext += new_char
        ciphertext += " "
        row = 1
        column += 1
      else:
        ciphertext += new_char
        row += 1
      if column > 10:
        ciphertext += "\n"
        column = 1
  return ciphertext

if __name__ == '__main__':
    shift = int(sys.argv[1])
    plaintext = input('Enter a message to encrypt: ')
    encrypted_message = caesar_cipher(shift, plaintext)
    print(encrypted_message)