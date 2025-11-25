class ToDo:
    title, desc = '',''
    
    def __init__(self, title, desc):
        self.title = title
        self.desc =desc
    
TODOS = []

def add(title, desc):
    global TODOS
    TODOS.append(ToDo(title, desc))

def delete_todo(index):
    global TODOS
    if index<0 or index>=len(TODOS):
        return
    TODOS = TODOS[:index] + TODOS[index+1:]

def edit_title(index, titile):
    global TODOS
    TODOS[index].title = title

def edit_desc(index, desc):
    global TODOS
    TODOS[index].desc = desc

def list_todos():
    global TODOS
    for i, todo in enumerate(TODOS):
        print(f"{i}. {todo.title}:\n{todo.desc}\n")


while (True):
    print()
    print("1. Add Todo")
    print("2. Delete Todo")
    print("3. Edit Todo")
    print("4. List Todo")
    print("0. Exit")

    choice = int(input("Enter choise: "))

    if choice == 1:
        title = input("Enter title: ")
        desc = input("Enter description: ")
        add(title, desc)
    elif choice == 2:
        index = int(input("Enter index: "))
        delete_todo(index)
    elif choice == 3:
        index = int(input("Enter index: "))
        title = input("Enter title, or keep blank for no change: ")
        desc = input("Enter description, or keep blank for no change: ")
        if title != "":
            edit_title(index, title)
        if desc != "":
            edit_desc(index, desc)
    elif choice == 4:
        list_todos()
    elif choice == 0:
        exit(0)
    else:
        print("Wrong choice")
