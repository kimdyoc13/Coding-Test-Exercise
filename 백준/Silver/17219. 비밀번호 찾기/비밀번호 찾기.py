# 구조

## 16만큼 입력 받음
# 딕셔너리 사용이 좋을것으로 보임

site_passward = {}
N, M = map(int, input().split())

for i in range(N):
    key, value = map(str, input().split())
    site_passward[key] = value

## 4만큼 입력 받으며 찾음

for i in range(M):
    A = str(input())
    print(site_passward[A])