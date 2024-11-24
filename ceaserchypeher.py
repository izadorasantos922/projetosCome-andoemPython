print("Let1s play a game ")
print(r"""
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   

      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|      
""")



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift, chipherdirection):
  new_text = ""
  if chipherdirection == "decode":
    shift *= -1;
  for letter in text:
    if letter in letters:
      position = letters.index(letter)
      new_position = (position + shift) % 26
      new_text += letters[new_position]
    else:
      new_text += letter
  print(f"Here's the {chipherdirection}d result: {new_text}")

shoul_end_game = False
while not shoul_end_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser(text= text, shift = shift, chipherdirection=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    shoul_end_game = True
    print("Bye!")

