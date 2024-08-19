# list=[1,2,3,4,5,6,7]
# for item in list :
#     print(item)

user = "Enter a  todo :"
todos= []
while True:
    user_action=input("type add, edit, show or exit:")
    match user_action.strip():
        case "add":
            todo=input("user :")
            todos.append(todo)
        case "show" :
            for item in todos:
                print(item.capitalize())
            # print(todos)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            # todos[number] = new_todo
            todos.__setitem__(number-1,input("Enter a todo"))
        case "exit" :
              break
print("Done!")


