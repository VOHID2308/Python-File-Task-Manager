from termcolor import colored


def print_menu():
    print("\n\n1. Kirish")
    print("2. Ro'yxatdan o'tish")


def print_sub_menu():
    print("\n\n1. Task Yaratish")
    print("2. Tasklarni ko'rish")
    print("3. Bajarilmagan tasklarni korish")
    print("4. Taskni bajarildi qilish")
    print("5. Chiqish")


def print_satus(text, status):
    types = {
        'error': 'red',
        'success': 'green'
    }
    colored_text = colored(text, types[status])
    print(colored_text)
    