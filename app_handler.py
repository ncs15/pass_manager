from hash_maker import password
import subprocess 
from database_manager import *
import pyperclip

default_mail='your default email'

class Manager:

    def app_menu(self):
        print('-'*30)
        print(('-'*13) + 'Menu'+ ('-' *13))
        print('1. Create new password')
        print('2. Find all sites and apps connected to an email')
        print('3. Find a password for a site or app')
        print('4. Show all passwords')
        print('5. Dump to txt')
        print('6. Delete entry by email and app/site name')
        print(' ')
        print('q. Exit')
        print('-'*30)
        return input(': ')

    def create(self):
       print('Please proivide the name of the site or app you want to generate a password for')
       app_name = input()
       print('Please provide a simple password for this site: ')
       plaintext = input()
       passw = password(plaintext, app_name, 15)
       print(passw)
       pyperclip.copy(passw)
       print('-'*30)
       print(' ')
       print('Your password has now been created and copied to your clipboard')
       print('')
       print('-' *30)
       user_email = input('Please provide a user email for this app or site(default)')
       if len(user_email) < 1:
           user_email = default_mail
       username = input('Please provide a username for this app or site (if applicable)')
       if username == None:
           username = '-'
       url = input('Please paste the url to the site that you are creating the password for')
       if url == None:
           url = '-'
       DB().store_passwords(passw, user_email, username, url, app_name)

    def find(self):
       print('Please proivide the name of the site or app you want to find the password to')
       app_name = input()
       DB().find_password(app_name)

    def find_accounts(self):
       print('Please proivide the email that you want to find accounts for')
       user_email = input()
       DB().find_users(user_email)

    def show_all(self):
        print("Your saved accounts are: ")
        DB().show_accounts()

    def dump(self):
        DB().fast_dump()

    def delete(self):
        mail=input("Enter the email: ")
        app=input("Enter the app/site name:  ")
        DB().delete_entry(mail,app)