CNP = input("Put your CNP : ")
# var = len(CNP)
if len(CNP) == 13 :
    print("Valid CNP")
elif len(CNP) <= 13 or len(CNP) > 13:
    print("Invalid CNP")