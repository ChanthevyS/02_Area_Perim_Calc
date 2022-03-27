# functions go here

# checks input is a number more than zero
def num_check(question):

    vaild = False 
    while not vaild:

        error = "Please enter a number that is more than zero"

        try:

            # asks user to enter a number
            response = float(input(question))
                
            # checks number is more than zero
            if response > 0:
                return response 

            # outputs error if input is invaild
            else: 
                print(error) 
                print()

        except ValueError:
            print(error)


# Main Routine goes here
width = num_check("Width: ")
height = num_check("Height: ")
print()
print("Width", width)
print("Height", height)
print()



