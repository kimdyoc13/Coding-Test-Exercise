def solution(s):
    
    oct_count = 0
    zero_value = 0
    
    while s != '1':
        zero_value += s.count('0')
        
        s = s.replace('0', '')
        
        s = format(len(s), 'b')
        oct_count += 1
    
    return [oct_count,zero_value ]