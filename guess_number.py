import random

def main(x): # for user to guess
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_num:
            print("Sorry! your guess is too high, try again,")
        elif guess < random_num:
            print("Sorry! your guess is too low, try again,")
    
    print(f'Yah, congrats. You have guessed the number{random_num} correctly!!')

def computer(x): # For the computer to guess
    low =1 
    high = x
    feedback =''

    while feedback != 'c':
        if low !=high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f'Is if {guess} too high (H), too Low (L),\
             or correct (C) ??').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess +1
        
    print(f'Yah, The computer guessed the number{guess} correctly!!')


computer(100)