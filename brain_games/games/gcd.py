def function_gcd():

    from brain_games.games.general import generate_random_number

    question = 'Find the greatest common divisor of given numbers.'
    number1 = generate_random_number()
    number2 = generate_random_number()

    correct_answer = str(max_divisor(number1, number2))
    expression = f'{number1}  {number2}'
    return question, expression, correct_answer


def max_divisor(a, b):
    while b:
        a, b = b, a % b
    return a