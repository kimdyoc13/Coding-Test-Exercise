def solution(n):
    list = []
    
    for i in range(n+1):
        if i % 2 ==0:
            list.append(i)
    
    return sum(list)