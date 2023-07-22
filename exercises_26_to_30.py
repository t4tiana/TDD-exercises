'''
26

Define a function which can compute the sum of two numbers.
'''

def sum_two(num1, num2):
  try:
    num1, num2 = int(num1), int(num2)
  except ValueError:
    print('Error: Numbers only!')
  except NameError:
    print('Error: Numbers only!')
  else:
    print(num1 + num2)

# Test 1 to ensure addition happens
sum_two(10, 235)

# Test 2 to see if exception is handled
sum_two('hi', 235)

'''
27

Define a function that can convert a integer into a string and print it in console.
'''

def int_to_str(num):
  num = str(num)
  print(num, type(num))

int_to_str(5)

'''
28
'''