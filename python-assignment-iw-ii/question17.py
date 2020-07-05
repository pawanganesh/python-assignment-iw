# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

try:
  num1 = int(input('Enter a number: '))
  num2 = int(input('Enter another number: '))

  operator = input('Enter operator: ')

  if operator == '+':
    print("{} {} {} = {}".format(num1, operator, num2, num1+num2))
  elif operator == '-':
    print("{} {} {} = {}".format(num1, operator, num2, num1-num2))
  elif operator == '*':
    print("{} {} {} = {}".format(num1, operator, num2, num1*num2))
  elif operator == '/':
    try:
      print("{} {} {} = {}".format(num1, operator, num2, num1/num2))
    except ZeroDivisionError:
      print('Cannot divide a number by zero')
  else:
    print("Enter valid numbers and operator")

except ValueError:
  print("Please enter integer")