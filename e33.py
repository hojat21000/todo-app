import glob

myfile=glob.glob("*.txt")
for filename in myfile:
    with open(filename,"r") as file:
        print(file.read())