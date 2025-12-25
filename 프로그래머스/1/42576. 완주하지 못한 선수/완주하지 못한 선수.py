def solution(participant, completion):
    count = {}
    
    # 받기
    for i in participant:
        count[i] = count.get(i, 0) +1
    
    # 검사
    for i in completion:
        count[i] = count.get(i, 0) -1
    
    for key, value in count.items():
        if value >0:
            return key