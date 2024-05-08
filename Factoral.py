number =int(input("Enter A number: "))#takes an input from the user
factorial = 1#states a variable and makes it one
while number > 1:# makes sure the number is over 0
    factorial = factorial * number#makes the factoral times the number variable
    number = number - 1#minuses 1 from the number
print(factorial)#prints the factoral
