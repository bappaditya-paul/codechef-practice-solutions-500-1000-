# cook your dish here
N = int(input())
arr = list(map(int, input().split()))
even_num = 0
odd_num =0
for element in arr:
    
    if element % 2 == 0:
        even_num +=1
    else:
        odd_num +=1
    
if even_num > odd_num:
   print("READY FOR BATTLE")
else:
    print("NOT READY")
