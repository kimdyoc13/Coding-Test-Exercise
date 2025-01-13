

# N 받기
N = int(input())

#N 만큼 단어 받기
word_list = []
for i in range(N):
    word = str(input())
    word_list.append(word)
#중복 제거

word_list = list(set(word_list))
# 정렬 기준으로 정렬
word_list.sort()

word_list = sorted(word_list, key = len)




# 출력
for i in word_list:
    print(i)