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

sidea = float(input("Enter the length of the first side of the triangle: "  ))
sideb = float(input("Enter the length of the second side of the triangle: "  ))
Area  = sidea * sideb
print("The area of the square/rectangel is: " + str(Area))

str1 = "Hello, World!"
str2 = "Python Programming"
print(str1 + " " + str2 )

list1 = [15, 25.26,95.45, 45.78]
list2 = ["apple", "banana", "cherry", "date"]

print(list1 + list2)
print (list1 * 2)
print(list1[2])
print(list2[1:3])
list1.append(55.67)
list1.sort()
print(list1)
list1.remove(25.26)
print(list1)
list1.pop(2)
print(list1)
list1.sort(reverse=True  )
print(list1)
list1.reverse()
print(list1)


#tuple
tuple1 = (10, 20, 30, 40, 50)
print(tuple1)
tuple2 = ("apple", "banana", "cherry", "date")
print(tuple2)
print(tuple1 + tuple2)
print(type(tuple1))
print(tuple1[1:3])
print(tuple2[0])
print(len(tuple1))
print(len(tuple2))

tuplepal = ["r", "a", "f"  "c", "a", "p"]
print(tuplepal)
copy_pal = tuplepal.copy()
print(copy_pal)
copy_pal.reverse()
if tuplepal == copy_pal:
    print("The tuple is a palindrome.") 
else:    print("The tuple is not a palindrome.")
