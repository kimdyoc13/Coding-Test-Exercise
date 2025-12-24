from collections import deque
def solution(arr):
    a = []
    answer = []
    arr= deque(arr)
    a.append(arr.popleft())
    answer.append(a[0])
    for i in range(len(arr)):
        if a[0] != arr[0]:
            a[0] = arr.popleft()
            answer.append(a[0])
        elif a[0] == arr[0]:
            arr.popleft()

    return answer