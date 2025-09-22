import prompt
import random 

ROUNDS_TO_WIN = 3

def ask_question(random_number):
    print(f'Question: {random_number}')
    

def run_game():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".') 
    while count < ROUNDS_TO_WIN:
        random_number = random.randint(0, 1000)
        ask_question(random_number)
        user_answer = prompt.string('Your answer: ')
        if (is_even(random_number) and user_answer == 'yes') or (not is_even(random_number) and user_answer == 'no'):
            print('Correct!')
            count += 1
            if count == ROUNDS_TO_WIN:
                print(f'Congratulations, {name}!')  
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{'yes' if is_even(random_number) else 'no'}'.")
            print(f"Let's try again, {name}!")
            return

def is_even(number):
    return number % 2 == 0
