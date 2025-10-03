#function to add two numbers
def add(a,b):
    return a+b

a = int(input("enter first number to add:" ))
b = int(input('Enter second number to add:' ))
print(add(a,b))

#function to check the Odd or Even  number
def if_odd_even(n):
    if n%2==0:
        return "Even"
    else :
        return "Odd"
c = int(input("Odd or even"))
print(if_odd_even(c))

#function to check the biggest number
def max(a,b,c):
    l1 = [a,b,c]
    return (min(l1))
d = int(input("enter number 1:"))
e = int(input("enter number 2:"))
f = int(input('enter number 3:'))
print(max(d,e,f))

#function to print table of a given number
def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

g = int(input("enter number for table:"))
table(g)

#function to print factorial of a  given number
def factorial(n):
    if n <= 1:
        return 1
    else:
        sum = n*factorial(n-1)
    return sum
h = int(input("Number for factorial:"))
print(factorial(h))