from hashlib import sha256
from printers import print_satus


def is_valid_username(username: str) -> bool:
    return username.isalpha()

def is_valid_password(password: str) -> bool:
    return len(password) >= 8

def is_same_password(password: str, confirm: str) -> bool:
    return password == confirm

def laod_users() -> list[dict]:
    with open('data/users.txt') as f:
        users = []
        for line in f.readlines():
            username, password = line[:-1].split(', ')
            users.append({
                'username': username,
                'password': password
            })

    return users

def add_user(username: str, password: str):
    with open("data/users.txt", "a") as f:
        f.write(f"{username}, {password}\n")

def make_password(password: str) -> str:
    hashed_password = sha256(password.encode()).hexdigest()
    return hashed_password


def is_username(username: str) -> bool:
    users = laod_users()
    return username in list(map(lambda user: user['username'], users))

def get_user(username: str, password: str) -> dict:
    users = laod_users()
    hashed_password = make_password(password)

    for user in users:
        if user['username'] == username and user['password'] == hashed_password:
            return user
    
    return None

def laod_tasks() -> list[dict]:
    with open('data/tasks.txt') as f:
        tasks = []
        for line in f.readlines():
            user, title, description, deadline, completed = line[:-1].split(', ')
            tasks.append({
                'user': user,
                'title': title,
                'description': description,
                'deadline': deadline,
                'completed': completed
            })

    return tasks

def create_task(user):
    title = input("title: ")
    description = input("description: ")
    deadline = input("deadline: ")

    task = {
        'user': user['username'],
        'title': title,
        'description': description,
        'deadline': deadline,
        'completed': "bajarilmagan"
    }
    tasks = laod_tasks()
    tasks.append(task)

    with open("data/tasks.txt", "a") as f:
        f.write(f"{user['username']}, {task['title']}, {task['description']}, {task['deadline']}, {task['completed']}\n")

    print_satus("task muvaffaqiyatli yaratildi", 'success')

def print_tasks(tasks):
    for counter, task in enumerate(tasks, start=1):
        print(f"{counter}. {task['title']}, {task['description']}, {task['deadline']}, {task['completed']}")

def show_tasks(user):
    tasks = laod_tasks()

    user_tasks = filter(
        lambda task: task['user'] == user['username'],
        tasks
    )
    print_tasks(user_tasks)

def show_incompleted_tasks(user):
    tasks = laod_tasks()

    user_tasks = filter(
        lambda task: task['user'] == user['username'] and task['completed'] == 'bajarilmagan',
        tasks
    )
    print_tasks(user_tasks)

def mark_as_completed(user):
    tasks = laod_tasks()

    user_tasks = list(filter(
        lambda task: task['user'] == user['username'] and task['completed'] == 'bajarilmagan',
        tasks
    ))

    print_tasks(user_tasks)

    i = int(input("qaysi taskni bajarildi qilmoqchisiz: ")) - 1
    target = user_tasks[i]

    with open("data/tasks.txt", "w") as f:
        for task in tasks:
            completed = ""
            if task == target:
                completed = 'bajarilgan'
            else:
                completed = task['completed']
            f.write(f"{task['user']}, {task['title']}, {task['description']}, {task['deadline']}, {completed}\n")

    print_satus("bajrildi", 'success')