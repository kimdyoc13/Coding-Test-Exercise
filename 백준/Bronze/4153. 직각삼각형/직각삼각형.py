while True: # ~~ 가 나올때까지
    num_list = list(map(int, input().split()))
    num_list.sort()
    if num_list[0] ==0:
        break
    elif num_list[0]**2 + num_list[1]**2 == num_list[2]**2:
        print("right")
    elif num_list[0]**2 + num_list[1]**2 != num_list[2]**2:
        print("wrong")