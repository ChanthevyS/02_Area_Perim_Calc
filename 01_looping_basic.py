vaild = False 
while not vaild:

    response = float(input("Enter a number: "))
    
    if response > 0:
       vaild = True

    else: 
        print("Please enter a number that is more than zero") 
        print()
