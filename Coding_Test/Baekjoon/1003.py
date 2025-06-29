"""
피보나치 식 
f(n) = f(n-1) + f(n-2)

"""

import sys

# 피보나치 수열 생성
fib_list = [0, 1]

for i in range(2, 41):
    fib_list.append(fib_list[i-1] + fib_list[i-2])


# T 받기
T = int(sys.stdin.readline().strip())

# 반복문으로 N 받기
for i in range(T):
    N = int(sys.stdin.readline().strip())
    



