#TowerOfHanoi.py
#Allen Liu
#August 15, 2018
#########################DESCRIPTION#########################
#A recursive tower of hanoi solver
#############################################################

#Represent each stack:
stacks = []
left = []
middle = []
right = []
stacks.append(left)
stacks.append(middle)
stacks.append(right)

#Disks represented by ints
def fill_stack(n):
    for i in range(n, 0, -1):
        left.append(i)

def print_stacks():
    print("{}{}{}".format(left, middle, right))

#Simple move
def move(start, end):
    stacks[end].append(stacks[start].pop())
    print_stacks()

#Simple two disk movement
def hanoi_2(start, middle, end):
    move(start, middle)
    move(start, end)
    move(middle, end)

#Hard coding until a pattern is found.
#I have no clue how but ok
def hanoi(start, middle, end, n):
    #1 stack:
    if n == 1:
        move(start, end)
    #2 stack
    if n == 2:
        hanoi_2(start, middle, end)
    #n stack
    elif n > 2:
        #Move all disks except for the largest to the middle
        hanoi(start, end, middle, n - 1)
        #Move largest
        move(start, end)
        #Repeat with the stack in the middle
        hanoi(middle, start, end, n - 1)

a = 10       
fill_stack(a)
print_stacks()
hanoi(0, 1, 2, a)


