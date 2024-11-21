def solution(answers):
    dic = { }
    correct = 0
    # 딕셔너리에 기록하면 되겠네

    first= [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third =  [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    person  = [first, second, third]
    for number, i in enumerate(person):
        correct = 0
        for x in range(len(answers)):
            # 각각 정답 갯수 기록
            if i[x] == answers[x]:
                correct += 1
        dic[number+1] = correct

    # 기록 완료, 그이후 dic 에서 value 가 가장 큰 값인 key 만 추출
    return [ k for k, v in dic.items() if max(dic.values()) == v]