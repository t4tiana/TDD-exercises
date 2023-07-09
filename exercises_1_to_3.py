'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.'''

def q1():
  for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
      print (i, end=',')

print(q1())

'''Write a program which can compute the factorial of a given number.The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be:40320'''

from functools import reduce
while True:
  try: 
    factorial = int(input("Put in a number to factorial: "))
  except ValueError:
    print ("Oops! Please enter a number.")
  else:
    answers = [int(factorial)]
    for n in range(1,int(factorial)):
      digit = int(factorial) - n
      answers.append(digit)
    total = reduce(lambda x,y: x*y, answers)
    print (f'The factorial of the number you entered is: {total}')
    break

'''With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8. 
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''
while True:
  try:
    n = int(input('Please input a number: '))
  except ValueError:
    print ("Oops! Please enter a number.")
  else:
    answers = dict()
    for num in range(1,(n+1)):
      answers[int(num)] = num*num
    print (f'The dictionary of your entry is: {answers}')
    break
##
# Author solution using dictionary comprehension
'''
n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)
'''

#My dict comprehension version
while True:
  try:
    n = int(input('Please input a number again: '))
  except ValueError:
    print ("Oops! Please enter a number.")
  else:
    ans = {i:i*i for i in range(1,(n+1))}
    print (f'Your dictionary is: {ans}')
  break