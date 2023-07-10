'''4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:'''
user_input = input('Go ahead and provide a list of numbers: ').split(',')
lst = []
for item in user_input:
  try:
    num = int(item)
  except ValueError:
    print ('Only your numbers are validated below.')
  else:
    lst.append(num)
print(lst)
tuple = tuple(lst)
print(tuple)


'''5. Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also include simple test function to test the class methods.'''

class Practice:
  def __init__(self):
    self.str1 = None

  def getString(self):
    self.str1 = str(input())

  def printString(self):
    print(self.str1.upper())


p1 = Practice()
p1.getString()
p1.printString()
#
#
'''6. Write a program that calculates and prints the value according to the given formula:

Q = Square root of [2*C*D / H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program: 100,150,180
Output = 18,22,24'''

'''First version
-
-

import math

entries = input('Enter some numbers: ')
value = entries.split(',')
list = [] #needs to be outside otherwise list is always reset each loop
for i in value:
  i = int(i)
  list.append(i)
ans = [] #needs to be outside otherwise list is always reset each loop
for integer in list:
  c = 50
  h = 30
  q = round(math.sqrt((integer*2*c) // h))
  ans.append(q)
print (ans)
'''
#Second go, where I made the code shorter
import math

entries = input('Enter some numbers: ')
value = entries.split(',')
list = [] #needs to be outside otherwise list is always reset each loop
c,h = 50,30
for d in value:
  d = int(d)
  q = round(math.sqrt((d*2*c) // h))
  list.append(q)
print (list)

'''One of the solutions that I liked because it is short without being vague.

my_list = [int(x) for x in input('').split(',')]
C, H, x = 50, 30, []

for D in my_list:
    Q = ((2*C*D)/H)**(1/2)
    x.append(round(Q))

print(','.join(map(str, x)))
'''
#
#
'''7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡Y-1. Suppose the following inputs are given to the program: 3,5:
Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''
## I don't even know what this is asking

'''8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
bag,hello,without,world
Then the output should be: bag,hello,without,world
'''

words = input('Provide some words separated by a comma: ').split(',')
words.sort()
print(words)

#

'''9. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Output = HELLO WORLD
PRACTICE MAKES PERFECT'''
#this is the author's answer because I couldn't get it to break from input
#it just kept letting me enter lines without moving on to the rest of the code
lst = []
while True:
    x = input('Gimme some lines: ')
    if len(x)==0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)
#tbh I could have thought of this. It was the len(x)==0 that I needed.