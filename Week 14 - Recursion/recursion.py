'''
General Info:
The process in which a function calls itself directly or indirectly is called recursion
and the corresponding function is called as recursive function. Using recursive algorithm,
certain problems can be solved quite easily. Examples of such problems are Towers of Hanoi,
Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.

For more info: https://www.geeksforgeeks.org/recursion/
'''
'''
Below is the Sample Code.
Driver code is the part of the code that actually runs.
- Uncomment the parts you want to run
- You can uncomment using ctrl/cmd + /
'''


'Part 1: Infinite Looping Recursion (results in an infinite recursion error)'
# def f():
#     print("hi")
#     f()

# 'Driver Code:'
# f()


'Part 2: Factorials'
'- Example 1: 3! = 3 * 2 * 1 = 6'
'- Example 2: 5! = 5 * 4 * 3 * 2 * 1'
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# 'Driver Code:'
# print(factorial(3))


'Part 3: Fibonacci Sequence'
'- First two numbers are 0 and 1'
'- Every number after that is the sum of the previous two Fibonacci Numbers'
'- First few numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21'
# print("haha u thought i would give you the answer to the challenge?")
# print("nice try")


'Part 4: Indirect Recursion'
# def indirect1(n):
#     if n == 0:
#         return
#     else:
#         print("this is the first function")
#         print(n)
#         indirect2(n-1)

# def indirect2(n):
#     if n == 0:
#         return
#     else:
#         print("this is the second function")
#         print(n)
#         indirect1(n-1)

# 'Driver Code'
# print(indirect1(5))

'''
Challenge(s):

Challenge 1 (Harder): Tower of Hanoi

    There are 3 rods an n disks.
    You must move an entire stack from the first rod to the third rod.
    However, there are 3 rules that you must follow...
    1. You can only move 1 disk at a time
    2. You can only move the uppermost disk on a stack and place it at the top of another disk
    3. A bigger disk cannot be placed an a smaller disk

    https://www.mathsisfun.com/games/towerofhanoi.html

    Example (2 disks):
    Let A, B, C be the names of the rods.
    Disk 1 moves from A to B
    Disk 2 moves from A to C
    Disk 1 moves from B to C

    Example (3 disks):
    Let A, B, C be the names of the rods.
    Disk 1 moves from A to C
    Disk 2 moves from A to B
    Disk 1 moves from C to B
    Disk 3 moves from A to C
    Disk 1 moves from B to A
    Disk 2 moves from B to C
    Disk 1 moves from A to C

    Create an algorithm that can solve the Tower of Hanoi!

Challenge 2 (Easy): Fibonacci Sequence
    Create an algorithm that will find the nth fibonacci number!
    Example: fib(10) = 34
    Example Explained: The first 10 fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. The 10th number is 34.
'''
