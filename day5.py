# 
# user = "Enter a  todo :"
# todos= []
# while True:
#     user_action=input("type add, edit, show or exit:")
#     match user_action.strip():
#         case "add":
#             todo=input("user :")
#             todos.append(todo)
#         case "show" :
#             for index,todo in enumerate(todos):
#                 print(index ," - ", todo.capitalize())
#             # print(todos)
#         case "edit":
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1
#             new_todo = input("Enter new todo: ")
#             # todos[number] = new_todo
#             todos.__setitem__(number-1,input("Enter a todo"))
#         case "remove":
#             number = int(input("Number of the todo to del: "))
#             number = number - 1
#             new_todo = input("Enter new todo: ")
#             # todos[number] = new_todo
#             todos.__setitem__(number - 1, input("Enter a todo"))
#         case "exit" :
#               break
# print("Done!")
# 



while True:
    user_action = input("type add, edit, show or exit:")
    match user_action.strip():
        case "add":
            todo = input("user :")
            todos.append(todo)
        case "show":
            for index, todo in enumerate(todos):
                print(index, " - ", todo.capitalize())
            # print(todos)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")


            # todos[number] = new_todo
            todos.__setitem__(number - 1, input("Enter a todo"))
        case "complet":
            number = int(input("Number of the todos to del: "))
            # number = number - 1
            del todos[number]
        case "exit":
            break
print("Done!")