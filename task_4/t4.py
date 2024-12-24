# Завдання 4

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

# Вимоги до завдання:
# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error.
# Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError.
# Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.

# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as err:
            return err
        except ValueError as err:
            return err
        except IndexError:
            return "Invalid command or missing arguments."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError("Contact not found")

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Give me name")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError("Contact not found")

@input_error
def show_all(contacts):
    if not contacts:
      raise ValueError("No contacts found")
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
