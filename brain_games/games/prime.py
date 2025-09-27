def function_prime():

    from brain_games.games.general import generate_random_number

    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = generate_random_number()
    correct_answer = 'yes' if all(
        number % i != 0 for i in range(2, int(number**0.5) + 1)
    ) and number > 1 else 'no'
    return question, number, correct_answer