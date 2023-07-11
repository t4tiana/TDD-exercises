'''16
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
output:
1,9,25,49,81'''

prompt = input('Enter a bunch of numbers separated by commas: ')
# .split could have been put at the end of input statement
squares = [int(x)**2 for x in prompt.split(',') if int(x)%2 == 1]
print(squares)

'''17
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
Where D is deposit and W is withdrawl
If the input is
D 300
D 300
W 200
D 100
Output = 500'''

total = []
transactions = []
while True:
    user_input = input()
    if user_input == '':
        break
    transactions.append(user_input + '\n')
for entry in transactions:
  if entry[0] == 'D':
    deposits = int(entry[2:])
    total.append(deposits)
  elif entry[0] == 'W':
    withdrawals = (-abs(int(entry[2:])))
    total.append(withdrawals)
print(total)
print('BALANCE: ', sum(total))

'''Example solution that I like because it uses strip instead of indexes.
Also, it is elegant to use the += this way

lst = []
while True:
  x = input()
  if len(x)==0:
    break
  lst.append(x)

balance = 0
for item in lst:
  if 'D' in item:
    balance += int(item.strip('D '))
  if 'W' in item:
    balance -= int(item.strip('W '))
print(balance)
'''