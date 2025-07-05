T = int(input())

for _ in range(T):
    X,Y,Z = map(int, input().split())
    if Z > (X*Y)/2:
        print("Yes")
    else:
        print("No")
