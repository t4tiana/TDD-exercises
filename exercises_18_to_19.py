'''18

A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1, 23E*, 2We3345

output = ABd1234@1'''

import re
import json

valid = []
# I want invalid passwords to be in a dictionary, so users see why
# the password was rejected
invalid = {}
while True:
  user_pw = input('Enter your passwords separated by a comma: ').split(', ')
  # Loop through each password submitted
  for entry in user_pw:
    # List that will be populated with validation errors
    err_list = []
    lower = re.search('[a-z]', entry)
    upper = re.search('[A-Z]', entry)
    digit = re.search('[0-9]', entry)
    symbol = re.search('[$#@]', entry)
    # Checking for each requirement individually to allow for 
    # multiple failures, instead of exiting loop on first fail
    if not lower:
      err_list.append('Missing at least 1 lowercase letter')
    if not upper:
      err_list.append('Missing at least 1 uppercase letter')
    if not digit:
      err_list.append('Missing at least 1 digit')
    if not symbol:
      err_list.append('Missing at least 1 symbol [$#@]')
    if len(entry) < 6 or len(entry) > 12:
      err_list.append('Not between 6 and 12 characters long')
      # Now that all requirements have been checked
      # Create dictionary where v = err_list
      invalid[entry] = err_list
    else:
      valid.append(entry)
  break
# Print not as pretty as I hoped but still better than default
print('VALID PASSWORDS:', json.dumps(valid, indent=2))
print('INVALID PASSWORDS:', json.dumps(invalid, indent=4))


'''19
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Output = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

lst = []
while True:
    tuples = input('Enter your name, age, and score separated by commas: ').split(',')
    # Break if no input
    if not tuples[0]:
        break
    lst.append(tuple(tuples))
# Data sorted by element priority 0>1>2 in accending order
print(lst)
  
