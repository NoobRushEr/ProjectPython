import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABETS = [char.upper() for char in alphabets]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']


def generate_password(length)->str:
    if length <= 4:
        print('Password Difficulty : WEAK')
    elif length <= 7:
        print('Password Difficulty : AVERAGE')
    elif 8 <= length <= 11:
        print('Password Difficulty : STRONG')
    elif length >= 12:
        print('Password Difficulty : TOO STRONG')



    Cap = random.choice(ALPHABETS)

    password_chars = (
        random.choice(alphabets) +
        random.choice(numbers) +
        random.choice(symbols)
    )

    all_chars = alphabets + ALPHABETS + numbers + symbols
    password_chars += ''.join(random.choices(all_chars, k=length - 4))

    password = ''.join(random.sample(password_chars, len(password_chars)))
    password = Cap+password
    return password


def validate_password(password)->bool:
    if len(password) < 4:
        return False

    has_upper = any(char in ALPHABETS for char in password)
    if not has_upper:
        print('Password should have one or more Uppercase characters.')

    has_symbol = any(char in symbols for char in password)
    if not has_symbol:
        print('Password should have one or more Special characters.')

    has_lower = sum(char in alphabets for char in password) >= 3
    if not has_lower:
        print('Password should have one or more Lowercase characters.')

    has_digit = sum(char in numbers for char in password) >= 3
    if not has_digit:
        print('Password should have one or more Digits.')

    return has_lower and has_upper and has_digit and has_symbol


def password_manager():
    print('Welcome to the Password Manager!')
    print('You can generate or Validate password.')
    while True:
        choice = input('Enter "g" to generate a password or "v" to validate a password or "t" to terminate application\n').lower()
        if choice.lower() == 'g':
            length = int(input('Enter the desired length of the password: '))
            password = generate_password(length)
            print(f'Generated Password: {password}')
        elif choice.lower() == 'v':
            password = input('Enter the password to validate: ')
            if validate_password(password):
                print('The password is valid.')
            else:
                print('The password is invalid.')
        elif choice.lower() == 't':
            print('Exiting Application...')
            print()
            break


if __name__ == '__main__':
    password_manager()