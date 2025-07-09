''' Sale Season

It's the sale season again and Chef bought items worth a total of X rupees. The sale season offer is as follows:

- If X ≤ 100, no discount.  
- If 100 < X ≤ 1000, discount is 25 rupees.  
- If 1000 < X ≤ 5000, discount is 100 rupees.  
- If X > 5000, discount is 500 rupees.

Find the final amount Chef needs to pay for his shopping.

Input Format                                                                                                     Output Format                                                           
The first line of input will contain a single integer T, denoting the number of test cases.                   For each test case, output on a new line the final amount Chef needs to pay for his shopping. 
Each test case consists of single line of input containing an integer X.

Constraints  
1 ≤ T ≤ 100  
1 ≤ X ≤ 10000

Sample Input       Sample Output   
4                   15
15                  70
70                  225
250                 975
1000

'''
# cook your dish here
T = int(input())

for _ in range(T):
    x = int(input())
    if x <= 100:
        print(x)
    elif 100 < x <= 1000:
        print(x-25)
    elif 1000 < x <= 5000:
        print(x-100)
    else:
        print(x-500)
        







