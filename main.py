"""
This module lets you play rock-paper-scissors!
"""
import random

def _computerchoice():
    choice = random.choices(['rock', 'paper', 'scissors'])
    return choice[0]

def _body():
    state = True

    while state:
        print('''
        Welcome to Rock-Paper-Scissors!
        Make your selection by typing "rock", "paper", or 
        "scissors", or type "quit" to quit.
        ''')
        user = input(': ').lower()
        if user == 'quit': break 
        elif user not in ('rock', 'paper', 'scissors'):
            print('\nInvalid choice.')
            continue
        computer = _computerchoice()
        print("\n%s vs %s" % (user, computer))
        if (user == 'rock' and computer == 'rock') or (user == 'paper' and computer == 'paper') or (user == 'scissors' and computer == 'scissors'): 
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
            print("You win!")
        else:
            print("You lose!")

_body()