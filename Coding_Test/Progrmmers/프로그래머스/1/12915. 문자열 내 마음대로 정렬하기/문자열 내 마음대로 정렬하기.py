def solution(strings, n):
    answer = []
    
    sorted_strings = sorted(strings, key = lambda x : (x[n], x))
    
    
    return sorted_strings