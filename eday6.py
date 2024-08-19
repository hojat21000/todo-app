# list=[1,2,4,5,8,8,9,6,3,3,7]
# for item in list :
#     print(item)
#
#     user = "Enter a todo :"
#     todos=[]
#     while True:
#         user_action=input("type add, show or exit :")
#         match user_action:
#              case "add":
#                  todo=input("Enter a todo :")
#                  todos.append(todo)
#              case "show":
#                 for index,todo  in enumerate(todos):
#                   print(index, " ", todo.capitalize())
#
#
#
#                  # for item in todos :
#                  #     print(item)
#                  # print(todos)
#              case "edit" :
#                  number = int(input("Enter a number ot the edit :"))
#                  number = number -1
#                  new_todo=input("Enter a new_todo ;")
#                  todos[number]= new_todo
#              case "complete":
#                  number = int(input("Enter a ot the  complete :"))
#                  number =number-1
#                  # del todos[number]
#                  todos.pop(number)
#              case "exit" :
#                  break
#
# list=[1,2,3,4,5,6,7,8,9,5,10,"hojat","ali","reza"]
# for index,list in enumerate(list):
#     print(index,"_",list)


size=int(input("Enter a size :"))
for i in range(1,size):
    for j in range(1,i):
         print(""*i ,end=" ")
    print("*"*size)
