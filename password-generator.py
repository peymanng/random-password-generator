import random
import string
import os
settings = {
    'lower': True,
    "upper": True,
    "symbol": True,
    "number": True,
    "space": False,
    "length": 8
}

PW_MIN_LEN = 4
PW_MAX_LEN = 30


def clear_screen():
    os.system("cls")


def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f"Include {option} ? (Defult is {default}) "
                           "(y : yes , n : no , Enter : default) ")
        if user_input == "":
            return default
        if user_input in ["y", "n"]:
            return user_input == "y"
        print("Invalid input. Please try again.")


def get_password_length(default, pw_min_len=PW_MIN_LEN, pw_max_len=PW_MAX_LEN):
    while True:
        user_input = input(f"password length ? (Default is {default}) "
                           "(enter : default value) ")
        if user_input == "":
            return default
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_len < user_password_length < pw_max_len:
                return int(user_input)
            print("Invalid input : You must enter a number between "
                  f"{pw_min_len} and {pw_max_len}")
        else:
            print("Invalid input : You must enter an integer number.")
        print("Please try again.")


def get_setting_from_user(settings):

    for option, default in settings.items():
        if option != "length":
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_len_choice = get_password_length(default)
            settings[option] = user_password_len_choice


def gen_random_char(choices):
    choice = random.choice(choices)

    if choice == "upper":
        return random.choice(string.ascii_uppercase)
    if choice == "lower":
        return random.choice(string.ascii_lowercase)
    if choice == "symbol":
        return random.choice(string.punctuation)
    if choice == "number":
        return str(random.choice(range(10)))
    if choice == "space":
        return " "


def want_another_password():
    while True:
        user_input = input(
            "do you want another password ? (y : yes , n : no) ")
        if user_input in ["y", "n"]:
            return user_input == "y"
        print("Invalid input , Try again.")


def password_generator(settings):
    final_result = ''
    password_length = settings["length"]

    choices = list(filter(lambda x: settings[x], [
                   "lower", "upper", "symbol", "number", "space"]))

    for _ in range(password_length):
        final_result += gen_random_char(choices)

    print(final_result)
    print("-" * 30)
    print("\n")
    user_want_another_password = want_another_password()
    print("\n")
    if user_want_another_password:
        password_generator(settings)


def run():
    clear_screen()
    get_setting_from_user(settings)
    print("-" * 30)
    password_generator(settings)

run()