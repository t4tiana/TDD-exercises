'''14
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!

Output = 
UPPER CASE 1
LOWER CASE 9'''

text = input('Give me a sentence: ')
text.replace(' ', '')
upper, lower = 0,0
for letter in text:
  if letter.isupper():
    upper += 1
  if letter.islower():
    lower += 1
print(f'UPPER CASE: {upper} \nLOWER CASE: {lower}')

'''Another option. Uses < because strings can be compared. And it still works even if your sentence has symbols like #$^#$

word = input()
upper,lower = 0,0

for i in word:
    if 'a'<=i and i<='z' :
        lower+=1
    if 'A'<=i and i<='Z':
        upper+=1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
'''

'''15
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program: 9
Then output: 11106'''

while True:
  digit = input("Input a digit from 1-9: ")
  try:
    num = int(digit)
    if num >= 1 and num <= 9:
      total = (num * 1) + (num *11) + (num *111) + (num*1111)
      print (total)
      break
    else:
      print ("That is too big a number! Try again.")
  except ValueError:
    print ("Try again! Digits 1-9 only.")

'''author solution using REDUCE method:

from functools import reduce

x = input('please enter a digit:')
reduce(lambda x, y: int(x) + int(y), [x*i for i in range(1,5)])

BECAUSE IF YOU MULTIPLY A STRING, like 'a' * 4 you get aaaa
'''