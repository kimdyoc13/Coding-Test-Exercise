def solution(s):
    # 빈스택 만들기
    stack = []
    
    for i in s:
        if i =='(':
            stack.append(i)
        else: 
            # 스택이 비어있으면
            if stack ==[]:
                return False
            # 스택이 차있으면
            else:
                stack.pop()
    
    if stack ==[]:
        return True
    if stack != []:
        return False
        
