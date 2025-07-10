''' Chefland Games
In Chefland, a tennis game involves 4 referees.
Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball is considered to be IN if and only if all the referees agree that it was inside limits.

Given the decision of the 4 referees, help Chef determine whether the ball is considered inside limits or not.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line of input containing 4 integers R1, R2, R3, R4 denoting the decision of the respective referees.
Here R can be either 0 or 1 where 0 would denote that the referee considered the ball to be inside limits whereas 1 denotes that they consider it to be outside limits.

Output Format
For each test case, output IN if the ball is considered to be inside limits by all referees and OUT otherwise.

The checker is case-insensitive so answers like in, In, and IN would be considered the same.
'''
T = int(input())
for _ in range(T):
    R1,R2,R3,R4 = map(int, input().split())
    if R1==1 or R2 ==1 or R3==1 or R4==1:
        print("OUT")
    elif R1==0 and R2==0 and R3==0 and R4==0:
        print("IN")
