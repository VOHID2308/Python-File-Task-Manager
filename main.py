from getpass import getpass
from printers import print_menu, print_satus, print_sub_menu
from utils import (
    is_valid_username, is_same_password, 
    is_valid_password, laod_users, 
    add_user, make_password,
    is_username, get_user,
    create_task, show_tasks,
    show_incompleted_tasks,
    mark_as_completed,
)


def main() -> None:
    user = None

    while True:
        print_menu()

        op = input("> ")
        if op == '1':
            username = input("username: ")
            password = getpass("password: ")

            user = get_user(username, password)
            if user:
                print_satus("muvaffaqiyatli kirdingiz.", 'success')

                while user:
                    print_sub_menu()
                    choice = input("> ")
                    if choice == '1':
                        create_task(user)
                    elif choice == '2':
                        show_tasks(user)
                    elif choice == '3':
                        show_incompleted_tasks(user)
                    elif choice == '4':
                        mark_as_completed(user)
                    elif choice == '5':
                        user = None
                    else:
                        print_satus("xato menu.", "error")
            else:
                print_satus("user topilmadi", 'error')
        elif op == '2':
            username = input("username: ")
            password = getpass("password: ")
            confirm_password = getpass("confirm password: ")

            if is_username(username):
                print_satus("bu username tanlangan.", "error")
            elif not is_valid_username(username):
                print_satus("username faqat harflardan iborat bolsin.", 'error')
            elif not is_valid_password(password):
                print_satus("pasrol kamida 8 ta belgigan iborat bolsin.", 'error')
            elif not is_same_password(password, confirm_password):
                print_satus("parol mos emas.", 'error')
            else:
                add_user(username, make_password(password))
                print_satus("ro'yxatdan otdingiz.", 'success')
        else:
            print("xato tanlov")

main()