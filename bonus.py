
def get_todos():
    with open("todos.txt", 'r') as file :
        todos=file.readlines()
    return todos

def set_todos(todos):
    with open('todos.txt','w') as file:
        todos=file.writelines(todos)









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




            # print("*" + " " + "*" + " " + "*")
            # for i in range(6):
            #     print("*"*(i))
            #
            #
            # for i in range(4):
            #     for j in range(4):
            #        print("*" * j, end=" ")
            #     print("*" * i, end=" ")
            #
            # size = 10
            # for i in range(0, size, 1):
            #      for j in range(0, i):
            #             print("*", end="")
            #      print()

            # for i in range(0,20,2):
    #         #     print(i)
    # size = int(input("Enter a size: "))
    # for i in range(1, size, ):
    #     for j in range(1, i):
    #         print(" ", end="")
    #     print("*" * size)

        # todos=[]
        # while True:
        #     todo=input("enter a todo:")
        #     todos.append(todo)
        #     print(todos)
        #
        # password=input("Enter a password :")
        # while password != "@ASDF":
        #     password=input("Enter a password :")
        # pirnt("password")
