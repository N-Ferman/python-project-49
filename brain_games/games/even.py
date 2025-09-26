
from brain_games.games.general import generate_random_number


def is_even(number):
    return number % 2 == 0


def function_even():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = generate_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, number, correct_answer






        


