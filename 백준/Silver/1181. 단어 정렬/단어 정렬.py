N = int(input())
word_list = []
for _ in range(N):
    word_list.append(str(input()))
    
word_list = list(set(word_list))

word_list.sort()
word_list = sorted(word_list, key = len)
    
for i in word_list:
    print(i)