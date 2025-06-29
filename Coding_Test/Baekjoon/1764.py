# 숫자 받기
def solution():
    N, M = map(int, input().split())
    # 문자열 차례로 받기
    A = []
    B = []

    for i in range(N):
        A.append(input())

    for i in range(M):
        B.append(input())


    # 중복 비교
    answer = []
    # for 문으로
    for i in A:
        if i in B:
            answer.append(i)

    # 출력
    print(len(answer))
    answer.sort()
    for i in answer:
        print(i)

solution()

