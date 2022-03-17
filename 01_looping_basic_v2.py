# checks that users enter a number that is more than zero
vaild = False 
while not vaild:

    error = "Please enter a number that is more than zero"

    try:

        # asks user to enter a number
        response = float(input("Enter a question: "))
            
        # checks number is more than zero
        if response > 0:
            vaild = True 

        # outputs error if input is invaild
         else: 
            print(error) 
            print()

    except ValueError:
        print(error)
