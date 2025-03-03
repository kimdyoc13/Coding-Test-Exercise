"""
점화식 : if i > 4 이면, 

d[i] = d[i-1] + d[i-2] + d[i-3]
"""


import sys

# 반복 수 받기
n = int(sys.stdin.readline())


# number_list 정의
number_list = [0, 1, 2, 4]

# number_list 10까지 정의
for i in range(4, 11):
    number_list.append(number_list[i-1] + number_list[i-2] + number_list[i-3])

# 찾아주기
for i in range(n):
    k = int(sys.stdin.readline())
    print(number_list[k])