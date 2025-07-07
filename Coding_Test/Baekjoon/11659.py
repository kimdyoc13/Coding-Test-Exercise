import sys

def prefix_sum(N):
    prefixSum = [0]*N
    prefixSum[0] = num_list[0]
    for i in range(1, N):
        prefixSum[i] = prefixSum[i-1] + num_list[i]
    return prefixSum


# 수의 개수 N 과 합을 구해야하는 횟수 M 받기
N, M  = map(int, input().split())
# N개의 개수 받기
num_list = list(map(int, sys.stdin.readline().split()))

prefixSum = prefix_sum(N)


# 구간 받기
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    if x != 1:
        print(prefixSum[y-1] - prefixSum[x-2])
    elif x==1:
        print(prefixSum[y-1])
    