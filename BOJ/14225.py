# Q. 14225
from itertools import product

n = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

a = 0
for i in num_lst:
    if a + 1 < i: 
        break
    a += i
    
print(a+1)