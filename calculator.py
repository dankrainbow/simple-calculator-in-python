## calculator
import os
from math import sqrt
import time
###

def slowtype(string):
  for letter in string:
    print(letter, end="", flush=True)
    time.sleep(0.05)

os.system("title Simple Calculator in python")
titletext = print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░▌          ▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ 
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌  
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  by dank rainbow
""")
def add(num1,numb2):
  answer = num1 +numb2 ## add the numbers
  return answer ## return the answer
def divide(num1,numb2):
  try:
    answer = num1/numb2 ## try dividing
    return answer ## then return the answer
  except ZeroDivisionError: ## except when trying to divide by zero, then send cant divide by zero
    print("Can't divide by zero!")
def subtract(num1,numb2): 
  answer = num1-numb2 ## subtract the numbers
  return answer ## return the answer
def multiply(num1,numb2):
  answer = num1*numb2 ## multiply
  return answer ## return answer
def squareroot(numb):
  answer = sqrt(numb) ## square root
  return answer ## return the answer

while True: ## forever do the following code
    print(titletext)
    print("Select operation.")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Square root")
    choice = input("Whats your choice: ") ## choice? 
    if choice == "1":
        first = float(input("First number: "))
        second = float(input("Second number: "))
        answer = add(first,second)
        slowtype(f"The answer is: {answer}\n") ## using the returned answer output the answer
    elif choice == "2":
        first = float(input("First number: "))
        second = float(input("Second number: "))
        answer = subtract(first,second)
        slowtype(f"The answer is: {answer}\n") ## using the returned answer output the answer
    elif choice == "3":
        first = float(input("First number: "))
        second = float(input("Second number: "))
        answer = multiply(first,second)
        slowtype(f"The answer is: {answer}\n") ## using the returned answer output the answer
    elif choice == "4":
        first = float(input("First number: "))
        second = float(input("Second number: "))
        answer = divide(first,second)
        slowtype(f"The answer is: {answer}\n") ## using the returned answer output the answer
    elif choice == "5":
        first = float(input("Number to square root: "))
        answer = sqrt(first)
        slowtype(f"The answer is: {answer}\n") ## using the returned answer output the answer
    repeat = input("Need another calculation (yes/no): ") ## check if another calculation is needed
    os.system("cls") ## clear the console before repeating
    if repeat == "no": ## if dont repeat
        slowtype("Thanks for using the calculator\n") ## say thanks
        break ## break the loop, ending the code
