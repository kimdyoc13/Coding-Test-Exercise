def solution(nums):
    answer = 0
    
    
    # process 
    # 중복 제거
    # nums 는 종류
    # 2/N 은 반환해야하는 갯수
    N = len(nums)
    nums = list(set(nums))
    
    if len(nums) >= N/2:
        return N/2
    elif len(nums) < N/2:
        return len(nums)
        