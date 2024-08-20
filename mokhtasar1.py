def get_hasans():
    with open("hasans.txt", 'r') as file :
        hasans=file.readlines()
    return hasans

def set_hasans(hasans):
    with open('hasans.txt','w') as file:
        hasans=file.writelines(hasans)


hasans=[]
while True:
    user_action=input("typeadd, show, edit, complete or exit :")

    if user_action.startswith("add"):
            hasan = user_action[4:]+"\n"

            hasans= get_hasans()
            hasans.append(hasan)

            hasans=set_hasans(hasans)
    elif user_action.startswith("show"):

            hasans = get_hasans()

            for index,item in enumerate(hasans):
                print(index+1,"--",item)
            # print(hasans_to_remove)
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            number =int(input("Enter a number of the edit"))
            number=number-1
            new_hasan=input("Enter a new_hasan:")+"\n"
            hasans[number] = new_hasan

            hasans = set_hasans(hasans)
        except ValueError:
            continue
    elif user_action.startswith("complete"):
        try:
              hasans = get_hasans()
              number = int(input(" Enter a number of the complete:"))
              number = number - 1
              # hasans_to_remove = hasans[number].strip("\n")
              h= hasans[number]
              del hasans[number]
              hasans = set_hasans(hasans)
              print(h)
        except "indexError":
         print(invalid)
    elif user_action.startswith("exit"):
            break
    else:
        print("kkkk")

