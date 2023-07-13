'''
22
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

ans = sorted(input().split())
my_dict = {}
for i in ans:
  my_dict[i] = ans.count(i)
for key in my_dict:
  print(key, ':', my_dict[key])
#
#
'''
23
Write a method which can calculate square value of number
'''

def squared(num):
  ans = num**2
  print(ans)

'''
24
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function
'''

import builtins 
def read_docs():
  '''This is a program that allows you to print the documents for built-in python functions. If you spell a function name incorrectly, you will be asked to try again or EXIT.'''
  print (read_docs.__doc__)

while True:
  x = input("Type the name of a built-in function or type read_docs to understand what this function does: ")
  if x == "read_docs":
    read_docs()
  else:
    if x in dir(__builtins__):
      print(help(str(x)))
      break
    if x == "EXIT":
      break
    else:
      print("No docs found! Check your spelling or choose a built-in function only. To exit, type EXIT")
  
'''
25
Define a class, which have a class parameter and have a same instance parameter.
'''

class Job:
    name = "Job"

    def __init__(self,name = None):
        self.name = name

dev=Job("Dev")
print("%s name is %s"%(Job.name,dev.name))

marketer=Job()
marketer.name="Marketer"
print("%s name is %s"%(Job.name,marketer.name))
