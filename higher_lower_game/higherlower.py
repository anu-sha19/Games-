from game_data import data
import random
from art import logo, vs
import os

game_over = False
score = 0

def compare():
    dictionary = random.choice(data)
    name=(dictionary['name'])
    occupation= dictionary['description']
    country = dictionary['country']
    followers = dictionary['follower_count']

    return name+ ',  ' + 'a '+ occupation+',  '+ 'from  ' + country + " " + str(followers)

first_person = (compare())

def play_game(first_person, score, game_over):
    while not game_over:
        slicing_A = int(first_person[-3:])
        second_person = compare()
        slicing_B = int(second_person[-3:])
        print(logo)
        print(f"Compare A: {first_person[:-3]}")
        print(vs)
        print(f"Compare B: {second_person[:-3]}")
        if first_person == second_person:
            second_person= compare()
        answer = input("Who has more followers? Type 'A' or 'B'").lower()
        if (slicing_A> slicing_B and answer == 'a')or (slicing_B > slicing_A and answer == 'b'):
            score+=1
            first_person = second_person
            print(f"You are right! Current score:{score}")
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry that's wrong. Final score: {score}")
            game_over = True

    
play_game(first_person, score, game_over)



    
