## calculator
from math import sqrt
def add(num1,numb2):
  answer = num1 +numb2
  print(f"The answer is: {answer}")
def divide(num1,numb2):
  try:
    answer = num1/numb2
    print(f"The answer is: {answer}")
  except ZeroDivisionError:
    print("Can't divide by zero!")
def subtract(num1,numb2):
  answer = num1-numb2
  print(f"The answer is: {answer}")
def multiply(num1,numb2):
  answer = num1*numb2
  print(f"The answer is: {answer}")
def squareroot(numb):
  answer = sqrt(numb)
  print(f"The answer is: {answer}")

print("""
Choose from the options below
1 - add
2 - divide
3 - subtract
4 - multiply
5 - square root
""")
choice = input()
if choice == "1":
  first = float(input("Enter first number: "))
  second = float(input("Second number: "))
  add(first,second)
elif choice == "2":
  first = float(input("Enter first number: "))
  second = float(input("Second number: "))
  divide(first,second)
elif choice == "3":
  first = float(input("Enter first number: "))
  second = float(input("Second number: "))
  subtract(first,second)
elif choice == "4":
  first = float(input("Enter first number: "))
  second = float(input("Second number: "))
  multiply(first,second)
elif choice == "5":
  number = float(input("number to square root: "))
  squareroot(number)
else:
  print("Invalid choice")