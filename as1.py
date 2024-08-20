# def get_hasans():
#     with open("haah/hasans.txt", 'r') as file :
#         hasans=file.readlines()
#     return hasans
#
# def set_hasans(hasans):
#     with open('haah/hasans.txt','w') as file:
#         hasans=file.writelines(hasans)
from mud import get_todos,set_todos
import time

from mud import get_hasans,set_hasans
import time

now =time.strftime("%a, %d %b %Y %H:%M:%S")
print("It is", now)




todos=[]
while True:
    user_action=input("typeadd, show, edit, complete or exit :")

    if user_action.startswith("add"):
            todo = user_action[4:]+"\n"
            # file=open('hasans.txt', 'w')
            # hasans=file.writelines(hasans)
            # file.close()
            # hasan = input("Enter a hasan:")+"\n"
            # hasans.append(hasan)
            # file=open('hasans.txt', 'r')
            # hasans=file.readlines()
            # file.close()
            todos= get_todos()
            todos.append(todo)
            # file = open('hasans.txt', 'w')
            # hasans = file.writelines(hasans)
            # file.close()
            todos=set_todos(todos)
    elif user_action.startswith("show"):
            # file = open('hasans.txt', 'r')
            # hasans = file.readlines()
            # file.close()
            todos = get_todos()

            for index,item in enumerate(todos):
                print(index+1,"--",item)
            # print(hasans_to_remove)
    elif user_action.startswith("edit"):
        try:
            todos=get_todos()
            number=int(user_action[5:])-1
            # number =int(input("Enter a number of the edit"))
            # number=number-1
            new_todo=input("Enter a new_todo:")+"\n"
            todos[number] = new_todo
            # file = open('hasans.txt', 'w')
            # hasans = file.writelines(hasans)
            # file.close()
            hasans = set_todos(todos)
        except ValueError:
            continue
    elif user_action.startswith("complete"):
        try:
              # file = open('hasans.txt', 'r')
              # hasans = file.readlines()
              # file.close()
              todos = get_todos()
              number = int(user_action[9:])- 1
              # number = int(input(" Enter a number of the complete:"))
              # number = numberinput - 1
              # hasans_to_remove = hasans[number].strip("\n")
              h= todos[number]
              del todos[number]
              # file = open('hasans.txt', 'w')
              # hasans = file.writelines(hasans)
              # file.close()
              todos = set_todos(todos)
              print(h)
        except indexError:
         print(invalid)
    elif user_action.startswith("exit"):
            break
    else:
        print("kkkk")




# file=open("fgfgfg.txt", "w")
# for i in range(10):
#     file.writelines(" %d  hojat askari big toooler  \r\n" %(i+1))
# file.close()
#
#
#
#
#
#
#
# hasans=[]
# while True:
#     user_action=input("typeadd, show, edit, complete or exit :")
#
#     if user_action.startswith("add"):
#             hasan = user_action[4:]+"\n"
#             # file=open('hasans.txt', 'w')
#             # hasans=file.writelines(hasans)
#             # file.close()
#             # hasan = input("Enter a hasan:")+"\n"
#             # hasans.append(hasan)
#             file=open('hasans.txt', 'r')
#             hasans=file.readlines()
#             file.close()
#             hasans.append(hasan)
#             file = open('hasans.txt', 'w')
#             hasans = file.writelines(hasans)
#             file.close()
#     elif "show" in user_action:
#             file = open('hasans.txt', 'r')
#             hasans = file.readlines()
#             file.close()
#
#             for index,item in enumerate(hasans):
#                 print(index+1,"--",item)
#             # print(hasans_to_remove)
#     elif user_action.startswith("edit"):
#             number=int(input("Enter a number of the edit:"))
#             number=number-1
#             new_hasan=input("Enter a new_hasan :")+"\n"
#             hasans[number] = new_hasan
#             file = open('hasans.txt', 'w')
#             hasans = file.writelines(hasans)
#             file.close()
#     elif "complete" in user_action:
#               file = open('hasans.txt', 'r')
#               hasans = file.readlines()
#               file.close()
#               number = int(input(" Enter a number of the complete:"))
#               number = numberinput - 1
#               # hasans_to_remove = hasans[number].strip("\n")
#               h= hasans[number]
#               del hasans[number]
#               file = open('hasans.txt', 'w')
#               hasans = file.writelines(hasans)
#               file.close()
#               print(h)
#     elif "exit" in user_action:
#             break
#     else:
#         print("kkkk")
#
#
#
# # file=open("fgfgfg.txt", "w")
# # for i in range(10):
# #     file.writelines(" %d  hojat askari big toooler  \r\n" %(i+1))
# # file.close()