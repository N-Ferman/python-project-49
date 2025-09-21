import prompt
def welcome_user():
    """Greet the user and ask for their name."""
    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')