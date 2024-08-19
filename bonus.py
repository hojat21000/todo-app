todos=[]
while True:
    user_action = input("type add,show, edit, complete or exit :")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo=input("Enter a todo : ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)

            file = open('todos.txt', 'w')
            todos = file.writelines(todos)
            file.close()
        case "show":

             file = open('todos.txt', 'r')
             todos = file.readlines()
             file.close()

             # todos=[item.strip('\n') for item in todos]
             for index,item in enumerate(todos):
                 item=item.strip("\n")
                 row = f"{index+1}--{item}"
                 print(row)
        case "edit":
                 number = int(input("Enter a number of the edit :"))
                 number = number - 1
                 new_todo = input("Enter a new_todo :")
                 todos[number] = new_todo
                 file = open('todos.txt', 'w')
                 todos = file.writelines(todos)
                 file.close()

        case "complete":
             # file = open('todos.txt', 'r')
             # todos = file.readlines()
             # file.close()
             number = int(input("Enter a number of the edit :"))
             number = number - 1
             del todos[number]
             file = open('todos.txt', 'w')
             todos = file.writelines(todos)
             file.close()
        case "exit":
            break