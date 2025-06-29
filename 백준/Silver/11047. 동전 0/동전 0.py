# 구조

# 데이터 받기
N, K = map(int, input().split())

# N = 10
# K = 4200
num_list = []
for i in range(N):
    num_list.append(int(input()))

# 계산

## 변수 지정
Count = 0
## N 보다 크지 않은 num 가져와서 
num_list = [x for x in num_list if x <= K]


## 그걸로 나누고 나머지로 계속 나누기
for i in range(len(num_list)):
    if K ==0:
        break
    value = num_list.pop()
    Count += K // value
    K = K % value
    
print(Count)




