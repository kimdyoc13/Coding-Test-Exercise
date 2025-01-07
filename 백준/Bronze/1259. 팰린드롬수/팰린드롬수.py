while True:
    # 받기
    N = str(input())
    # 거르기
    if int(N) == 0:
        break
    
    # Yes, No 판별
    if N == N[::-1]:
        print("yes")
    else:
        print("no")