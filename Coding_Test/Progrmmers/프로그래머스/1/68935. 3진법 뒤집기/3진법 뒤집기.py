def solution(n):
    
# 삼진법 변환
    def trans(n, q):
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)

        return rev_base[::-1] 
        # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
        
    n = trans(n, 3)
    # 앞 뒤 뒤집기

    n = n[:: -1]

    # 십진법 표현

    answer = int(n,3)
        
    return answer
    
    

