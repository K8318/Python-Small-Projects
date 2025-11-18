#empty dictionary
contacts = {}

while True:
    print('\n contact Book App')
    print('1. create contact')
    print('2. view contact')
    print('3. update contact')
    print('4. delete contact')
    print('5. Search contact')
    print('6. count')
    print('7. exit')

    # noinspection PyRedeclaration
    choice: int = int(input('Enter your choice: '))
    if choice == '1':
        name = input('Enter your name: ')
        if name in contacts:
            print(f'Contact with {name} already exists!')
        else:
            age: int = int(input('Enter your age: '))
            email = input('Enter your email: ')
            mobile = input('Enter your mobile number: ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact name {name} has been created successfully')

    elif choice == '2':
        name = input('Enter contract name to view =: ')
        if name in contacts:
            contact = contacts[name]
            print(f"name:{name}, Age:{age}, Mobile:{mobile}")
        else:
            print('Contact does not exist')

    elif choice == '3':
        name = input('Enter name update contact =')
        if name in contacts:
            age: int = int(input('Enter updated age: '))
            email = input('Enter updated email: ')
            mobile = input('Enter update mobile number: ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
        else:
            print('Contact does not found!')

    elif choice == '4':
        name = input('Enter your name delete contact =')
    if name in contacts:
        del contacts[name]
        print(f'Contact with {name} has been deleted successfully!')
    else:
        print('Contact does not exist')

        elif choice == '5':
            search_name = input('Enter contact name to search = ')
            found = False
            for name,contact in contacts.items():
            if search_name.lower() == in name.lower():
                print(f'found - Name {name}, Age:{age}, Mobile:{mobile}, Email:{email}')
                found = True
            if not found:
                print('No contact found with this name')

    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')

    elif choice == '7':
        print('Good bye......Closing the program')
        break

    else:
    print('invalid choice')

