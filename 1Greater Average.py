
T = int(input())

for _ in range(T):
    a,b,c = map(int, input().split())
    
    if (a+b)/2 > c:
        print("Yes")
    else:
        print("No")
