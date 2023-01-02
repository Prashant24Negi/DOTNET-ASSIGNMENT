user_number = int(input("Enter the size of your triangle: "));

for i in range(user_number):

    for k in range(user_number-i-1):
        print(" ", end="");
        
    for j in range(2*i+1):
        print("*",end="")
    print()