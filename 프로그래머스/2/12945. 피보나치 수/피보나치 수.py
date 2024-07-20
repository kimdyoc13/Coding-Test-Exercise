def solution(n):
    # 피보나치 수 0, 1 리스트 정의
    number_list = [0, 1]
    
    # 반복문을 순회하며 피보나치 수 리스트에 추가
    for i in range(2, n+1):
        number_list.append(number_list[i-2] + number_list[i-1])
    
    # 결과값 출력
    return number_list[-1] % 1234567