# 컴퓨터수 입력 받기
computer_number = int(input())

graph = {}

for i in range(1, computer_number+1):
    graph[i] = []
# 네트워크 노드 갯수 입력 받기
node = int(input())



for i in range(node):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)




def dfs(graph, start_node):
 
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
 
    ## 시작 노드를 시정하기 
    need_visited.append(start_node)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
 
            ## 그 노드에 연결된 노드를 
            need_visited.extend(graph[node])
            
    return visited

print(len(dfs(graph, 1)) -1)