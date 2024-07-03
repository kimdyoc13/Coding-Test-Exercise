def solution(a, b, n):
    
    new = 0
    # while 문으로 반복
    # n == empty 병
    # while 문 안에서 n(empty)에서 a 빼고  new 와 n(empty) b 를 더함
    while n >= a:
        # x 는 빈병을 새병으로 교환하는 수
        x = n // a

        # n 만큼 뺴기
        n = n - (x * a)
        # 새 병수 더하기
        new += (x * b)

        # 새병을 빈병으로 바꿀때 수 더하기
        n += (x * b)
        
        
    return new