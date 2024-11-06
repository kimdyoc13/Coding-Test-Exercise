def solution(x):
    x_list = []
    
    for i in str(x):
        x_list.append(int(i))
    
    t = sum(x_list)
    
    if x % t ==0:
        answer = True
    elif x % t!=0:
        answer = False
    return answer