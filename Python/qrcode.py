name = input("Enter the name of the person: ")
if name == "Nikhil":
    print("Hello, Nikhil! Welcome back!")
else:    
    print("Hello, " + name + "! Nice to meet you!")

number1 = [1,2,3,4,5]
squares = [x**2 for x in number1]
print("The squares of the numbers are: " + str(squares))

a = input("Enter the first number: ")
b = input("Enter the second number: ")
result = int(a) + int(b)
print("The sum of " + a + " and " + b + " is: " + str(result))