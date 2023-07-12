'''
20
Define a class with a generator that can iterate the numbers, all divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program: 7
Output: 
0
7
14
'''

class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) + 1):
            yield i * 7

for i in MyGen().by_seven(int(input('Please enter a number... '))):
    print(i)

'''
21
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. 

If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2

Output = 2
'''

import math

x,y = 0,0

while True:
  ans = input('Please enter the directions or type END: ')
  if ans == "END":
    break
  else:
    coord = ans.split(' ')
    if coord[0] == 'UP':
      y += int(coord[1])
    if coord[0] == 'DOWN':
      y -= int(coord[1])
    if coord[0] == 'LEFT':
      x -= int(coord[1])
    if coord[0] == 'RIGHT':
      x += int(coord[1])

dist = round(math.sqrt(x**2 + y**2)) #needed to be down here otherwise x,y = 0,0 still
print(dist)