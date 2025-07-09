import sys
# 방향 벡터
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 변수 정의
answer = 0

# dfs 함수 정의
def dfs(M, N):
    
    for i in range(N):
        for j in range(M):
            if vegetable_list[i][j]== 1:
                need_visited = [[i, j]]

                while need_visited:
                    cy, cx = need_visited.pop()
                    if vegetable_list[cy][cx] ==1:
                        vegetable_list[cy][cx] = 0 # 방문 처리
                        for d in range(4):
                            ny, nx = cy + dy[d], cx + dx[d]
                            if 0 <= ny <N and 0 <=nx < M and vegetable_list[ny][nx] ==1:
                                need_visited.append([ny, nx])
                global answer
                answer += 1 
T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    ## 빈 리스트 만들기

    vegetable_list = [[0 for x in range(M)] for x in range(N)]

    # 일부 리스트 받기
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        vegetable_list[y][x] = 1
    
    #------------------------------------------------------------------------
    dfs(M, N)


    #------------------------------------------------------------------------------

    print(answer)
    answer = 0