#Hangman game
import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
display = []
for i in range(len(chosen_word)):
         display+= "_"
end_game = False
lives=5
print(f"{logo} \n {stages[6]} \n {chosen_word}")
print(f"{' '.join(display)}")
while not end_game:
       guess = input("Guess a letter of the word:\n")
       if guess in display:
                print(f"You've already guessed {guess}")
       for j in range(len(chosen_word)):
          if(chosen_word[j]==guess):
            display[j] = guess
       if guess not in chosen_word:
            print(f"Oops you guessed {guess}, that's not in the word. You lose a life \n {stages[lives]}")
            lives -=1
       print(f"{' '.join(display)}")
       if '_' not in display :
          end_game = True
          print(" Awesome, there is the Winner Congratsss!!")
       if lives==-1:
           end_game =True
           print("GAME OVER! Your man has been hanged!")







