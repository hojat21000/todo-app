user="Enter a todo :"
todos=[]
while True:
    user_action=input("type add,edit,show,complete or exit :")
    match user_action:
        case "add":
           todo=input(user)
           todos.append(todo)
        case "show":
           print(todos)
        case "edit":
            number=int(input("Enter a number of the edit :"))
            number =number-1
            new_todo=input("Enter a new_todo :")
            todos[number]=new_todo
        case "complete":
            number = int(input("Enter a number of the edit :"))
            number = number - 1
            del todos[number]
        case "exit":
            break
            