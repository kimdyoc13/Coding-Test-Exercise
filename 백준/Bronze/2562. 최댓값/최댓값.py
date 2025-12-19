A = {}
for i in range(1, 10):
    A[i] = int(input())

sorted_A = sorted(A.items(), key = lambda item:item[1], reverse=True)
print(sorted_A[0][1])
print(sorted_A[0][0])