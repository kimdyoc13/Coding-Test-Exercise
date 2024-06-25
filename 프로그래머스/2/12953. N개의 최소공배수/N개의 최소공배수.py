def solution(arr):
    answer = 0
    k = 0
    arr = sorted(arr)
    x = 1
    for n in arr:
        x *= n
    
    for i in range(1, x + 1):
        for j in arr:
            if i  % j ==0:
                continue
            k = 1
        if k ==0:
            answer = i
            break
        k = 0
    return answer