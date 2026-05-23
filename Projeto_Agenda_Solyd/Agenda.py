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

# show_contacts()
search_contact("João", "Giovana", "Rafael", "Maria")