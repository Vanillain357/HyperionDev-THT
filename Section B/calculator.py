# this program is a simple calculator that takes 2 numbers and an opperator
# the program has been written defensively and should handle anything the user throws at it

# create a dictionary to turn the users opperator from a string into a function
opperators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

# defining a function to check for various errors in the user's string
def error_check(equation_str):
# split the string into a list, seperating at every " "    
    equation = equation_str.split(" ")
        
# if the list is shorter than 3, display an error    
    if len(equation) < 3:
        print("You don't seem to have entered 2 numbers and an opperator. Did you remember the spaces?")
# if the list is longer than 3, display an error    
    elif len(equation) > 3:
        print("Sorry, I can only handle 2 numbers and 1 operator for now.")
# if the middle value is not one of the 4 opperators, display an error    
    elif equation[1] not in opperators:
        print("Sorry, that is not a valid opperation")
# if the user tries to divide by 0, display an error    
    elif (equation[1] == "/") and (equation[2] == "0"):
        print("Sorry, I'm not allowed to divide a number with zero.")
# check that both numbers are infact ints    
    else:
        try:
            int(equation[0]), int(equation[2])
            return ("okay")
# if either of the user's numbers are not integers, display an error    
        except ValueError:
            print("Sorry it seems that at least one of your numbers are not integers")

# defining a function to solve the equation
def solve(equation_str):
# split the equation into a list, seperating at every " "    
    equation = equation_str.split(" ")
# use the apropriate function from the dictionary to try and solve the equation
# the middle value is used as the function and the first and last values are passed to it     
    return round(opperators[equation[1]](int(equation[0]), int(equation[2])), 2)

    
# defining a function to write down any valid opperations and their answer
def write_down(equation_str, file = "history.txt"):
# open "history.txt"
    with open(file, "a") as ofile:
# write the equation and the answer using the solve function        
        ofile.write(f"{equation_str} = {solve(equation_str)}\n")
    
# print some instructions for the user
print("Welcome to the improved calculator app, now with exception handling!\n\n"\
    "Please enter a simple mathematical opperation formatted as such: <num1> <opperator> <num2>\n"\
    "Please also make sure to seperate the numbers and opperators with a space \" \"\n"\
    "Currently the only opperators available are [+, -, *, /]\n\n"\
    "Alternatively you can write the name of a txt file and I'll display all of the equatioins in that file.\n"\
    "*HINT* by default I store everything you do in \"history.txt\"")

# a while loop is used so that the user can keep entering equations
# if the equation is valid, the answer will be displayed, otherwise an error will be displayed
while True:
# get the user's equation    
    equation_str = input("\n:")

# if the user enters the name of a txt file, try and read that file    
    if ".txt" in equation_str:
        try:
# if it exists, display all of the equations in the file            
            with open(equation_str, "r") as ifile:
                print(f"Here are all the equations in {equation_str}:", ifile.read().strip("\n"), sep = "\n")
# if not, display an error        
        except FileNotFoundError:
                print("Sorry, it does not seem like that file exists. Try \"history.txt\"")

# if the user enters an equation call the error_check, solve, and write_down functions to solve and document the equation    
    else:
        if error_check(equation_str) == "okay":
            print(solve(equation_str))
            write_down(equation_str)