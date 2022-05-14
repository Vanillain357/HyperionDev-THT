# this program demonstrates a function to test the validity of 10 or 13 digit ISBN codes
# if a 10 digit code is valid it will be converted into a 13 digit code

def isbn13(isbn):
# create a list of expected characters an ISBN number should consist of (strings of numbers 0 through 9)    
    expected_chars = []
    for i in range(10):
        expected_chars.append(str(i))
# add "X" as a 10 digit ISBN can end on an X
    expected_chars.append("X")
    
# if any character in the string is not in the list, print "Invalid"    
    for char in isbn:
            if char not in expected_chars:
                print("Invalid")
                return

    isbn_sum = 0
# contruct 2 lists of ints that the numbers will be lined up with 
    multipliers13 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    multipliers10 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# cast the string to a list of ints (at this point we know it will not cause an error)    
    isbn_nums = []
    for char in isbn:
# if the character is an "X" append 10       
        if char == "X":
            isbn_nums.append(10)
        else:
            isbn_nums.append(int(char))

# if the number is 13 digits, line it up with "multipliers13" and get the sum of the product of each number and its multiplier    
    if len(isbn_nums) == 13:
        for i in range(13):
            isbn_sum += (multipliers13[i] * isbn_nums[i])

# if the sum is divisable by 10, print "Valid", if not, print "Invalid"
        if isbn_sum % 10 == 0:
                print("Valid")
        else:
                print("Invalid")

# if the number is 10 digits long, line it up with "multipliers10" and again get the sum of the products    
    elif len(isbn_nums) == 10:
        for i in range(10):
            isbn_sum += (multipliers10[i] * isbn_nums[i])

# if the sum is divisable by 11 it is a valid 10 digit code and needs to be converted
        if isbn_sum % 11 == 0:
# tack on the numbers            
            converted10 = [9, 7, 8] + isbn_nums
            isbn_sum = 0
            
# reperform the calculation to get the sum of the products            
            for i in range(13):
                isbn_sum += (multipliers13[i] * converted10[i])
            remainder = isbn_sum % 10

# if the 10 digit code ended on an X, sub in "0"            
            if converted10[-1] == 10:
                converted10[-1] = 0
            
# if there is no remainder after dividing by 10, leave the check-digit unchanged           
            if remainder == 0:
                 for char in converted10:
                     converted10_string += (str(char))
            
# if there is a remainder, make the check-digit equal to 10 - the remainder            
            else:           
                converted10[12] += 10-remainder
                converted10_string = ""
                for char in converted10:
                    converted10_string += (str(char))            
            print(converted10_string)
        else:
            print("Invalid")
    else:
        print("Invalid")

# test the function
isbn13("033030142X")
isbn13("0316066524")
isbn13("0330301824")
isbn13("9780316066525")
isbn13("9780316066526")
isbn13("978031606652")