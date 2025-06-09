import random

def get_random_numbers() -> (int, int):
    lower_limit, upper_limit = 1, 100
    try:
        lower_limit = int(input('What should be the Lower Limit:\n'))
        upper_limit = int(input('What should be the Upper Limit:\n'))
    except ValueError as e:
        print('')
    return lower_limit, upper_limit

def get_tries() -> int:
    tries = 5
    try:
        tries = int(input('How many chances do you need to guess the Number?\n'))
    except ValueError:
        print('')
    return tries

def check_number(guess, number)->bool:
    if guess > number:
        print('LOW')
    if guess < number:
        print('HIGH')
    return True if guess == number else False

def number_guesser():
    lower_limit, upper_limit = get_random_numbers()
    number = random.randint(lower_limit,upper_limit)

    tries = get_tries()

    found = False
    while tries > 0:
        print(f'Remaining Tries : {tries}')
        guess = int(input("Guess the Number\n"))
        found = check_number(guess, number)
        if found:
            print('Congrats..! Number is found.')
            print(f'Number is {guess}.')
            break
        tries-=1

    if not found:
        print("Unfortunately, you couldn't find the number.")
        print(f'Number was {number}.')
    print('GAME OVER...')

if __name__ == '__main__':
    number_guesser()