'''Minimum Pizzas
Each pizza consists of 4 slices. There are N friends and each friend needs exactly X slices.

Find the minimum number of pizzas they should order to satisfy their appetite.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two integers N and X, the number of friends and the number of slices each friend wants respectively.

Output Format
For each test case, output the minimum number of pizzas required.
'''
T = int(input())

for _ in range(T):
    N,X = map(int, input().split())
    total = N*X 
    result = total % 4
    if result == 0:
        print(total // 4)
    else:
       print((total //4)+1)
