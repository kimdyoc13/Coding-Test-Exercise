def solution(s):
    answer = ''
    # 문자 나누기
    s = s.split(' ')    
    # 대 소 문자 변환
    for i in s:
        for index, j in enumerate(i):
            if index % 2 ==0:
                answer += j.upper()
            elif index % 2 ==1:
                answer += j.lower()
                
        # 대소문자 합치기
        
        answer += ' '
    
            
    return answer[:-1]