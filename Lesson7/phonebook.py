# Создать телефонный справочник с возможностью импорта и
# экспорта данных в нескольких форматах.

def main():

    import library
    from os import system

    system('cls')

    FILENAME_CSV = 'phonebook.csv'
    FILENAME_TXT = 'phonebook.txt'
    FIELDS = ['Full name', 'Phone', "Description"]
    FIELD_FULL_NAME = 0
    FIELD_FHONE = 1
    choice = int()
    while choice != 6:

        choice = library.show_menu()

        system('cls')

        if choice == 1:
            library.display_the_phone_book(FILENAME_CSV, FIELDS)
        elif choice == 2:
            library.find_contact(FILENAME_CSV, FIELDS, FIELD_FULL_NAME)
        elif choice == 3:
            library.find_contact(FILENAME_CSV, FIELDS, FIELD_FHONE)
        elif choice == 4:
            library.add_contact(FILENAME_CSV, FIELDS)
        elif choice == 5:
            library.save_phone_book_in_txt_file(
                FILENAME_CSV, FILENAME_TXT, FIELDS)


if __name__ == '__main__':
    main()
