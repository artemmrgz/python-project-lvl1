import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play(name, generate_question, calculate):
    game_rounds = 3
    while game_rounds:
        question = generate_question()
        user_answer = prompt.string('Your answer: ')
        correct_answer = calculate(question)
        if correct_answer == user_answer:
            print('Correct!')
            game_rounds -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            break
    if not game_rounds:
        print(f'Congratulations, {name}!')
