from app_handler import *
from secret import password


def login():
    secret = password.get_password()
    passw = input('Please enter the password: ')
    if passw == secret:
        print('Logged in!')

    else:
        print('Incorrect password!')
        exit()

def main():
    manager = Manager()
    choice = manager.app_menu()
    while choice != 'q':
        if choice == '1':
            manager.create()

        if choice == '2':
            manager.find_accounts()

        if choice == '3':
            manager.find()

        if choice == '4':
            manager.show_all()

        if choice == '5':
            manager.dump()

        if choice == '6':
            manager.delete()

        else:
            choice = manager.app_menu()
        choice = manager.app_menu()



if __name__ == "__main__":
    login()
    main()