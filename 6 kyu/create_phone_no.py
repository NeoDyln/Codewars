def create_phone_number(n):
    
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!
    
    
    
#     First I converted all the numbers to characters and kept them in a string
    tempString = ""
    for num in n:
        tempString += str(num)
#     I then got the length of the string
#       Remember len in python counts from 1
    pLen = len(tempString)
    
#     I then created a final string that will add the parenteses, spaces and hyphen at the desired positions on top of adding the characters, otherwise, I just add the character at that position
    finString = ""
#     i acts as a counter of sorts to help me identify where I need to add the parentheses / spaces / hyphens
    i = 1
    while i < pLen+1:
        if i == 1:
            finString += "("
        if i == 4:
            finString += ") "
        if i == 7:
            finString += "-"
        finString += tempString[i-1]
        i += 1
    return finString
