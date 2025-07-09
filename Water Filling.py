'''Water Filling

Chef has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if at most one bottle is empty, she will wait, and not fill them up now.

You are given three integers - B1, B2, and B3.  
If B1 = 1, it means that the first bottle is full.  
If B1 = 0, it means that the first bottle is empty.  
Similarly, B2 denotes whether the second bottle is full or empty, and B3 denotes it for the third bottle.

Output "Water filling time", if Chef has to fill the bottles now. If not, output "Not now".

Input Format  
The first line of input will contain a single integer T, denoting the number of test cases.  
The only line of each test case contains three space-separated integers, B1, B2, B3.

Output Format  
For each test case, output on a new line, either "Water filling time", or "Not now".

Constraints  
1 ≤ T ≤ 1000  
Bi is either 0 or 1

Sample Input  
5  
0 0 0  
1 1 1  
1 1 0  
0 1 0  
0 1 1

Sample Output  
Water filling time  
Not now  
Not now  
Water filling time  
Not now
'''
# cook your dish here
T = int(input())

for _ in range(T):
    B1,B2,B3 = map(int,input().split())
    total = B1+B2+B3
    if total <= 1:
        print("Water filling time")
    else:
        print("Not now")
       


