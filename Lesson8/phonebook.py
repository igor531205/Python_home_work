# Создать телефонный справочник.

from os import system

from library import *


def main():

    FILENAME_CSV = 'phonebook.csv'
    FILENAME_TXT = 'phonebook.txt'

    SHOW_MENU = {1: f'"Display the phone book"',
                 2: f'"Find contacts by full name"',
                 3: f'"Find contacts by phone number"',
                 4: f'"Add contact to phone book"',
                 5: f'"Remove contact from phone book"',
                 6: f'"Update contact in phone book"',
                 7: f'"Export "json" phone book to {FILENAME_TXT}"',
                 8: f'"Exit the program"'
                 }

    FIELDS = ['full name', 'phone number', "description"]

    FIELD_FULL_NAME = FIELDS.index('full name')
    FIELD_FHONE_NUMBER = FIELDS.index('phone number')

    choice = int()
    while True:

        print(*[f'\r{key}. {value}\n' for key, value in SHOW_MENU.items()])

        FIRST_ITEM = 1
        choice = SHOW_MENU.get(user_input_number('Enter menu item number -> ',
                                                 FIRST_ITEM, len(SHOW_MENU)))
        system('cls')

        # Display the phone book
        if choice == SHOW_MENU.get(1):
            display_the_phone_book(FILENAME_CSV, FIELDS)

        # Find contacts by full name
        elif choice == SHOW_MENU.get(2):
            find_contact(FILENAME_CSV, FIELDS, FIELD_FULL_NAME)

        # Find contacts by phone number
        elif choice == SHOW_MENU.get(3):
            find_contact(FILENAME_CSV, FIELDS, FIELD_FHONE_NUMBER)

        # Add contact to phone book
        elif choice == SHOW_MENU.get(4):
            add_contact(FILENAME_CSV, FIELDS)

        # Remove contact from phone book
        elif choice == SHOW_MENU.get(5):
            remove_contact_from_phone_book(FILENAME_CSV, FIELDS,
                                           FIELD_FULL_NAME)

        # Update contact in phone book
        elif choice == SHOW_MENU.get(6):
            update_contact_in_phone_book(FILENAME_CSV, FIELDS,
                                         FIELD_FULL_NAME)

        # Export phone book to txt file
        elif choice == SHOW_MENU.get(7):
            save_phone_book_to_txt_file(FILENAME_CSV, FILENAME_TXT, FIELDS)

        else:
            break
        print()


if __name__ == '__main__':
    # system('pip install -r requirements.txt')
    system('cls')
    main()
    system('pip freeze > requirements.txt')
