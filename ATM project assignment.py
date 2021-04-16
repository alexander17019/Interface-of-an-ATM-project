import random

import datetime

x = datetime.datetime.now()
print(x)

database = {
    1315936386: ["alex", 'bakare', 'alex@gmail', 'qwerty' , 0 ]

}

balance = []


def init():
    print("Welcome to bankPHP")
    have_account = int(input("Do you have account with us: (1) yes (2) no  \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()
    else:
        print("You have selected invalid option")

    init()


def login():
    print("******** Login *******")

    account_number_from_user = int(input("What is your account number?  \n"))
    password = input("What is your password  \n")

    for account_number, user_details in database.items():
        if account_number == account_number_from_user:
            if user_details[3] == password:
                bank_operation(user_details)

    print("Invalid account or password")
    login()


def register():
    print("***** Register******")

    email = input("what is your email address?  \n")
    first_name = input("what is your first name  \n")
    last_name = input("what is your last name?   \n")
    password = input("create a password for yourself  \n")

    account_number = generation_account_number()

    database[account_number] = [first_name, last_name, email, password, 0]

    print("Your Account Has been created")
    print("++++++++ ++++ +++++")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print("++++++ +++++ ++++++++")

    login()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do today? (1) deposit (2) withdrawal (3) Logout (4) Exit  \n"))

    if selected_option == 1:

        deposit_operation()

    elif selected_option == 2:

        withdrawal_operation(user)
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    print("withdrawal")

    selected_option = int(input("would you like to ? (1) Get current balance (2) amount to withdrawal (3) exit  \n"))

    if selected_options == 1:

        set_current_balance(user)

    elif selected_options == 2:

        amount_withdrawal()

    elif selected_options == 3:

        bank_operation(user)

    else:
        print("Invalid Option selected")

        bank_operation(user)


def deposit_operation():
    print("Deposit Operations")

    selected_option = int(input("Would you like to ? (1) get current balance (2) amount to deposit (3) exit  \n "))

    if selected_option == 1:
         set_current_balance(user)

    elif selected_option == 2:
        amount_deposit()

    elif selected_option == 3:
        bank_operation(user)

    else:
        print("Invalid Option selected")
        bank_operation()


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def amount_withdrawal():
    return random, randrange(1111, 9999)

def amount_deposit():
    return int("amount to deposit")

def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_account_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
