'ATM pin check'
pin= 1234
for i in range (1,4):
    n= int(input("Enter 4 digit Pin= "))
    if n==pin:
        print("Welcome")
        break
    else:
        print(f"Incorrect Pin. Attempt left: {3-i}\n")
if (i==3):
    print("To many attemps. Your Card is blocked..")
