N = int(input())

info = []
for i in range(N):
    A, B = map(str, input().split())
    A = int(A)
    info.append((A, B))
# key 기준 오름차순
sorted_info = sorted(info, key = lambda item: item[0])

for key, value in sorted_info:
    print(key, value)
    