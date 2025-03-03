"""
아이디어

점화식 : An = An-1 + An-2
"""



import sys



n = int(sys.stdin.readline())

# n = int(input())

rs = [0, 1, 2]

for i in range(3, n+1):
    rs.append( (rs[i-1] + rs[i-2] ) % 10007)


print(rs[n])
