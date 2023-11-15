"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random

def guess_the_number():
  num = random.choice([1,2,3,4,5,6,7,8,9])
  res= 0
  print (num)
  while res != num:
    print("Guess the number (1-9):")
    print("Por favor, ingresa un número: ")
    res = input()
    res = int(res)
  
  print(f"El numero es {num}")
  
  """
    Using loops, implement a guessing game.
    Guess the number (1-10):
    messages: Too low, Too high, Try again, Congratulations!
  """
  # fix code
  # num = 0;
  # numero = random.randint(0, 10);
  # while num != numero:
  #   print("Guess the number (1-10):");
  #   num = input();
  #   num = int(num)
  #   if num < numero:
  #     print("Too low");
  #   elif num > numero:
  #     print("Too high");
  #   elif num == numero:
  #     print("Congratulations!");
  #   else:
  #     print("Try again");
      


def multiplication_table():
  num = random.choice([1,2,3,4,5,6,7,8,9])
  for i in range(1,11):
    tbl = num*i
    print(f"{i} x {num} = {tbl}")



def basic_calculator():
  """
    Using a while/for loops, implement a basic calculator.
    1. Enter the first number: 10
    2. Enter an operator (+, -, *, /): +
    3. Enter the second number: 20
    4. print 10 + 20 => Result: 30
  """
  num1 = input("Enter the first number: ")
  operator = input("Enter an operator (+, -, *, /): ")
  num2 = input("Enter the second number: ")

  result = None # fix code

  print("{num1} {operator} {num2} => Result:", result)


def main():
  # input choice between 1-3 function
  # call the function
  choice = int(input(f"""
    1. Guess the number
    2. Multiplication table
    3. Basic calculator
    Enter a number (1-3): """))
  if choice == 1:
    guess_the_number()
  elif choice == 2:
    multiplication_table()
  elif choice == 3:
    basic_calculator()
  else:
    print("Invalid choice.")

main()