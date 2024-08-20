
date = input("Enter today's date :")
mode = input("how do you rate your mod today from 1 to 10?")
thoughts = input("let your thoughts flow:\n")

with open(f"../journal/{date}.txt","w") as file:
   file.write(mod+2*"\n")
   file.write(thoughts)
