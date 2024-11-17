import random
easywords = ["casa", "mesa", "bolo", "fogo", "vaca", "muro"]
mediumwords = ["banana", "carroça", "camelo", "boneca", "panela", "amigo"]
hardwords = ["maravilhoso", "computador", "televisão", "bicicleta", "universidade", "harmonioso"]

print("Let's play a game \n")
print(r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

# Imagens do jogo corrigidas com raw strings
HANGMANPICS = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']




chose = input("Easy, medium or hard? ").lower()
word = [];
current_index = 0
actualhangmanpic = HANGMANPICS[current_index];
if(chose == "easy"):
    word = random.choice(easywords)
    print(word)
elif(chose == "medium"):
    word = random.choice(mediumwords)
elif(chose == "hard"):
    word = random.choice(hardwords)
else:
    print("Invalid, try again!")
    exit()

display = ["_" for _ in word];
print("\n")
print(" ".join(display))
print(actualhangmanpic)

while "_" in display:
    guess = input("Digite uma letra: ").lower()

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess
    else:
        print("Letra incorreta!")
        if current_index < len(HANGMANPICS) - 2:
            current_index += 1;
            actualhangmanpic = HANGMANPICS[current_index]
        else: 
            print("\n")
            print("You lose!")
            print(HANGMANPICS[len(HANGMANPICS) - 1])
            exit()
    print(" ".join(display))
    print(actualhangmanpic)

print(f"Parabéns! Você adivinhou a palavra: {word}")