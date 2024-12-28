#INTRODUCTION
def intro(name):
    print("Hello,Good morning! I am",name)
user_name=input("Enter your name:")
intro(user_name)

#FACTORIAL
def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
num=int(input("Enter a number"))
#check if number is negative
if num<0:
    print("Sorry,factorial doesnot exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",recur_factorial(num))

#Calculator using function

#this function adds two number
def add(x,y):
    return x+y
#this function substracts two number
def substract(x,y):
    return x-y
#this function multiplies two number
def multiply(x,y):
    return x*y
#this function divides two number
def divide(x,y):
    return x/y
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
print("Sum: " ,add(num1,num2))
print("Difference: " ,substract(num1,num2))
print("multiply: " ,multiply(num1,num2))
print("Divide: " ,divide(num1,num2))