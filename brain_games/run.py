
from brain_games.games.calc import function_calc
from brain_games.games.cli import welcome_user
from brain_games.games.even import function_even
from brain_games.games.gcd import function_gcd
from brain_games.games.general import (
    ROUNDS_TO_WIN,
    ask_question,
    get_user_answer,
    is_correct_answer,
    print_congratulations,
    print_correct,
    print_question,
    print_wrong,
)


def choose_game():
    print('Please choose a game:')
    print('1 - Even')   
    print('2 - Calc')
    print('3 - GCD')
    name_game = int(input())
    match name_game:
        case 1:
            return function_even
        case 2:
            return function_calc
        case 3:
            return function_gcd
        case _:
            return None


def run_game():
    game_function = choose_game()
    if game_function is None:
        print('This game is not available.')
        return
    
    count = 0
    name = welcome_user()
    
    while count < ROUNDS_TO_WIN:
        question, expression, correct_answer = game_function()
        if (count == 0):
            print_question(question)
        ask_question(expression)
        user_answer = get_user_answer()
        if (is_correct_answer(correct_answer, user_answer)):
            print_correct()
            count += 1
            print_congratulations(count, name)
            
        else:
            print_wrong(user_answer, correct_answer, name)
            return