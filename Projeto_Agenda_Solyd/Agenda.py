import os
SCHEDULE = {}

def validate_string(func): # Decorator for add and delete params
    def wrapper(*args):
        for value in args:
            if value is not None and not isinstance(value, str):
                print(f'>>>>> {value} must be a string')
                return
        return func(*args)
    return wrapper

def show_contacts(contact_name=None):
    if contact_name:
        contacts = {contact_name: SCHEDULE[contact_name]}
    else:
        contacts = SCHEDULE
    # This make the search_contacts() uses this function
    for contact, data in contacts.items():
        print('Name:', contact)
        print('Number:', data['number'])
        print('Email:', data['email'])
        print('Address:', data['address'])
        print('-' * 50)

def search_contact(*args):
    for contact in args:
        if contact in SCHEDULE:
            show_contacts(contact)
        else:
            print(f'>>>>> Contact "{contact}" not found.')
            print('-' * 50)

@validate_string
def add_or_edit_contact(name, number, email, address):
    action = "updated" if name in SCHEDULE else "added"
    old_contact = SCHEDULE.get(name, {})
    # This is for make the function remember the old data
    # of the contact

    SCHEDULE[name] = {
    "number": number if number is not None else old_contact.get("number", ""),
    "email": email if email is not None else old_contact.get("email", ""),
    "address": address if address is not None \
        else old_contact.get("address", "")
    }
    print(f">>>>> Contact {name} {action} with success")
    save()

@validate_string
def delete_contact(name):
    if name in SCHEDULE:
        SCHEDULE.pop(name)
    else:
        print(f'>>>>> Contact {name} not found')
        return
    print(f' >>>>> Contact {name} deleted ')
    save()

def export_contacts(file_name):
    try:
        with open(file_name, 'w') as file:
            # file.write('name,number,email,address\n')
            for contact, data in SCHEDULE.items():
                number = data['number']
                email = data['email']
                address = data['address']
                file.write(f'{contact},{number},{email},{address}\n')
        if not file_name == 'database.csv':
            print('>>>>> Schedule exported with success')
    except Exception as error:
        print('>>>>> An error occurred while trying to export the contacts.')
        print(error)

def import_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, number, email, address = line.strip().split(',')
                add_or_edit_contact(
                    name,
                    number,
                    email,
                    address
                )
        print('>>>>> Contacts imported with success')
    except FileNotFoundError:
        print('>>>>> File not found')
    except Exception as error:
        print(">>>>> An error occurred while trying to import the contacts.")
        print(error)

def save():
    export_contacts('Projeto_Agenda_Solyd/database.csv')
def load():
    try:
        with open('Projeto_Agenda_Solyd/database.csv', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, number, email, address = line.strip().split(',')
                    SCHEDULE[name] = {
                        'number': number,
                        'email': email,
                        'address': address
                    }
    except Exception as error:
        print(">>>>> An error occurred while trying to load the contacts.")
        print(error)



def print_menu():
    print('------------------------------------------')
    print('1 - Show all contacts')
    print('2 - Search contact')
    print('3 - Add contact')
    print('4 - Edit contact')
    print('5 - Delete contact')
    print('6 - Export contacts to CSV')
    print('7 - Import contacts from CSV')
    print('0 - Close schedule')
    print('------------------------------------------')

# Start of program
if __name__ == '__main__': 
    load()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print_menu()
        option = input('Escolha uma opção: ')

        match option:
            case '1':
                show_contacts()
            case '2':
                name = input('Contact name: ')
                search_contact(name)
            case '3' | '4':
                name = input('Contact name: ')
                number = input('Contact number: ')
                email = input('Contact email: ')
                address = input('Contact address: ')
                add_or_edit_contact(name, number, email, address)
            case '5':
                name = input('Contact name: ')
                delete_contact(name)
            case '6':
                file_name = input('CSV File name: ')
                print('Exporting Schedule...')
                export_contacts(file_name)
            case '7':
                file_name = input('CSV File name: ')
                print('Importing Schedule')
                import_contacts(file_name)
            case '0':
                print('Closing Schedule...')
                break
            case _:
                print('Invalid Option')

        input('\nPress [ENTER] to continue...')
        # It controls the loop