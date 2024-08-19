# x=1
# while x<=10 :
#     print(x)
#     x=x+1
# #     password_admin="@12345"
# password=input("Enter your password:")
# while password != "@12345" :
#   password = input("Enter your password :")
# print("your password is currect !!")


#
# user_prompt="Enter a todo:"
# todos=[]
# while True:
#     todo=input(user_prompt)
#     todos.append(todo)
#     print(todos)


user_prompt="Enter a todo:"
todos=[]
while True:
    user_action=input("type add,show or exit: ")

    match user_action:
        case "add":
            todo=input("Enter a todo:")
            todos.append(todo)
        case"show":
            for item in todos :
            
                print(item)
            print(todos)
        case "exit":
            break
print("Done!")
