ROUNDS_TO_WIN = 3


def ask_question(expression):
    print(f'Question: {expression}')


def generate_random_number():
    import random
    return random.randint(0, 100)


def get_user_answer():
    import prompt
    return prompt.string('Your answer: ')


def print_correct():
    print('Correct!')


def print_congratulations(count, name):
    if count == ROUNDS_TO_WIN:
        print(f'Congratulations, {name}!')


def print_wrong(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def print_question(string):
    print(string)


def is_correct_answer(correct_answer, user_answer):
    return correct_answer == user_answer