import pickle

def save_to_file(email_dict):
    with open('emails.pickle', 'wb') as f:
        pickle.dump(email_dict, f)

def load_from_file():
    try:
        with open('emails.pickle', 'rb') as f:
            return pickle.load(f)
    except:
        return {}

def main():
    email_dict = load_from_file()
    while True:
        print('1. Look up a person\'s email address')
        print('2. Add a new name and email address')
        print('3. Change an existing email address')
        print('4. Delete an existing name and email address')
        print('5. Quit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            name = input('Enter the name: ')
            if name in email_dict:
                print(f'Email address: {email_dict[name]}')
            else:
                print('Name not found')
        elif choice == 2:
            name = input('Enter the name: ')
            if name in email_dict:
                print('Name already exists')
            else:
                email = input('Enter the email address: ')
                email_dict[name] = email
        elif choice == 3:
            name = input('Enter the name: ')
            if name in email_dict:
                email = input('Enter the new email address: ')
                email_dict[name] = email
            else:
                print('Name not found')
        elif choice == 4:
            name = input('Enter the name: ')
            if name in email_dict:
                del email_dict[name]
            else:
                print('Name not found')
        else:
            save_to_file(email_dict)
            break


main()
