#Декоратор, який обробляє помилки
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Incomplete command. Provide all necessary arguments."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Функція, яка додає контакт до словника контактів
@input_error
def add_contact(args, contacts): 
    name, phone = args
    contacts[name] = phone
    return "Contact added."

 # Функція, яка змінює існуючий контакт у словнику контактів
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

 # Функція, яка показує номер телефону для вказаного імені
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else: 
        return f"The name {name} is not on your contacts list yet."

#Функція, яка виводить всі збереженні контакти з номерами телефонів
@input_error
def show_all(contacts):
    res = ""  

    if len(contacts) == 0:
        return "Your contact list is empty."
    else:
        for name, phone in contacts.items():
            res += f"{name}: {phone} \n"
        return res.rstrip("\n")  

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":  
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()