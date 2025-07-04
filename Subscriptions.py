T = int(input())

for _ in range(T):
    N,X = map(int, input().split())
    
    if N % 6 == 0:
        subscriptions = (N//6)

    else:
        subscriptions = (N//6+1)
        
    total_cost = subscriptions*X
    print(total_cost)
