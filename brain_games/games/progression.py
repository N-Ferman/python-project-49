def function_progression():
    import random

    from brain_games.games.general import generate_random_number

    question = 'What number is missing in the progression?'
    start = generate_random_number()
    step = generate_random_number()
    length = 10
    hidden_index = random.randint(0, length - 1) #NOSONAR
    progression_list = [str(start + step * i) for i in range(length)]
    correct_answer = progression_list[hidden_index]
    progression_list[hidden_index] = '..'
    expression = ' '.join(progression_list)
    return question, expression, correct_answer