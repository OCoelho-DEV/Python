SCHEDULE = {
    'Rafael': {
        'number': '(21) 3559-8336',
        'email': 'rafaelemail@gmail.com',
        'address': 'Av. 1'
    },

    'Giovana': {
        'number': '(21) 2052-7460',
        'email': 'giovanaemail@gmail.com',
        'address': 'Av. 2'
    }
}

def validate_string(func):
    def wrapper(*args):
        for value in args:
            if value is not None and not isinstance(value, str):
                print(f'{value} must be a string')
                return
        return func(*args)
    return wrapper

def show_contacts(contact_name=None):
    if contact_name:
        contacts = {contact_name: SCHEDULE[contact_name]}
    else:
        contacts = SCHEDULE

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
            print(f'Contact "{contact}" not found.')
            print('-' * 50)

@validate_string
def add_or_edit_contact(name, number, email, address):
    action = "updated" if name in SCHEDULE else "added"

    old_contact = SCHEDULE.get(name, {})

    SCHEDULE[name] = {
    "number": number if number is not None else old_contact.get("number", ""),
    "email": email if email is not None else old_contact.get("email", ""),
    "address": address if address is not None \
        else old_contact.get("address", "")
    }
    print(f">>>>> Contact {name} {action} with success")





# show_contacts()
# search_contact("João", "Giovana", "Rafael", "Maria")
# add_or_edit_contact("João", "22222" ,"joaoemail", "address")
# add_or_edit_contact("Rafael", "22222" ,"rafaelemail", None)
# add_or_edit_contact("foo", "22222" ,"fooemail", None)
show_contacts()

