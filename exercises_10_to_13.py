'''10
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
-- hello world and practice makes perfect and hello world again
output should be:
-- again and hello makes perfect practice world'''

#This time, I practiced combining functions and methods to reduce lines
prompt = input()
thisset = set(prompt.split(' '))
lst = sorted(list(thisset))
print (' '.join(word for word in lst))

'''11
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. Assume the data is input by console.
input: 0100,0011,1010,1001
output should be: 1010 
'''
prompt = input().split(',')
# list = prompt.split(',')
for number in prompt:
  number = int(number)
  number = bin(number)
  if number % 5 == 0:
    print (number, end=',')
# a binary is a string
# you have to do something with bases and powers. I couldnt solve it.
## solution below
print(*(binary for binary in input().split(',') if int(binary,base=2)%5==0))

'''12
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.'''

for i in range(999,3000):
    string = str(i)
    if int(string[0]) % 2 == 0 and int(string[1]) % 2 == 0 and int(string[2]) % 2 == 0 and int(string[3]) % 2 == 0:
      print (string, end = ',')
    else:
      continue

'''13
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123
output = LETTERS 10
DIGITS 3'''

import re

phrase = input('Input phrases and numbers: ')
total_letters = []
total_numbers = []
joined = phrase.replace(' ', '')
for letter in joined:
    x = re.findall('[a-zA-Z]', letter)
    y = re.findall('\d', letter)
    if x:
      total_letters.append(x)
    if y:
      total_numbers.append(y)

  
print(f'LETTERS: ', len(total_letters))
print(f'DIGITS: ', len(total_numbers))

'''Their solution using isalpha and isnumeric therefore no need for regex:

word = input()
letter, digit = 0,0

for i in word:
    if i.isalpha(): # returns True if alphabet
        letter += 1
    elif i.isnumeric(): # returns True if numeric
        digit += 1
print(f"LETTERS {letter}\n{digits}") 
'''