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

dict1 = {"name": "Nikhil", "age": 25, "city": "New York"}
print(dict1)
dict2 = {"name": "Alice", "age": 30, "city": "Los Angeles"}
print(dict2)    
print(dict1["name"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get("age"))
print(dict1.update({"age": 26}))
print(dict1)

dictionary = {
    "table":["list of facts and figures","a piece of furniture"],
    "cat":"a small animal"
}
print(dictionary.items())

setexample = {1, 2, 3, 4, 5}
print(setexample)
setexample.add(6)
print(setexample)
setexample.remove(3)
print(setexample)
setexample.discard(10)
setexample.clear()
print(setexample)
print("cleared")

setexample1 = {1, 2, 3,8,9,6,5}
setexample2 = {4, 5, 6,7,8,9}
setunion= setexample.union(setexample1)
print(setunion)
setintersection = setexample1.intersection(setexample2)
print(setintersection)

count =1
while count <= 5:
 print("Count: " + str(count))
 count = count + 1

table = 5
count = 1
while count <= 10:
  result = table * count
  print("table:",table, "x", count, "=", result)
  count = count + 1

num9 = (1, 2, 3, 4, 5,6,8,9,7,53,4,3,24)
i=0
m=33
while i<len(num9):
    while num9[i] == m:
      print("Found the number: " + str(m))
      break
    print(num9[i])
    i = i + 1


list67 = [1, 2, 3, 4, 5,34,43,54,65,76,87,98,9]
list68 = [234,345,54,456,657,575,77,678,6786,7868]
char = "nikhilkulaprorira"

for i in list67:
    if (i == 34):
        print(i)

for r in range(2,5,2):
    print("Hello, World!")

print("Hello, World!")
print("Starting of loop and recusrion   example")


def sum (a,c,b):
  return a+b+c
 
sum1 = sum(5, 10, 15)
print("The sum of the numbers is: " + str(sum1))

list55 = [1, 2, 3, 4, 5,7]
def noofelemints(lst):
    return len(lst)
print(noofelemints(list55))

def printinsingleline(lst):
    for i in lst:
        print(i, end=" ")
printinsingleline(list55)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def recur_sumofnnaturalno(n):
    if n <= 0:
        return 0
    else:
        return n + recur_sumofnnaturalno(n - 1  )
print(recur_sumofnnaturalno(88))


print("Starting of file I/O operations example")
f = open("C:\\Users\\nikhi\\project\\Python\\testingfile.txt", "rw")
data = f.read()
f.write("This is a new line added to the file.")
print(data)
f.close()