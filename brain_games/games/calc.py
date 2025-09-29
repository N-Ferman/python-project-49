 
def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(a, b, sign):
    match sign:
        case '+':
            return add(a, b)
        case '-':
            return subtract(a, b)
        case '*':
            return multiply(a, b)
        case _:
            return None
            

def function_calc():
    import random

    from brain_games.games.general import generate_random_number

    question = 'What is the result of the expression?'
    number1 = generate_random_number()
    number2 = generate_random_number()
    sign = random.choice(['+', '-', '*'])  # NOSONAR
    correct_answer = str(calculate(number1, number2, sign))
    expression = f'{number1} {sign} {number2}'
    return question, expression, correct_answer