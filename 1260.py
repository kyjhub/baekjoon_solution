from collections import deque

N, M, V = map(int, input().split())

graph=[[] for _ in range(N+1)]
for _ in range(M):
  a, b=map(int, input().split())      # 연결된 노드 입력
  graph[a].append(b)                  # a와 연결된 노드를 a번째 리스트에 입력
  graph[b].append(a)                  # b와 연결된 노드를 b번째 리스트에 입력

for i in range(1, N+1):
  graph[i].sort()                     # 노드와 연결된 노드들 중 작은 수에 해당하는 노드들부터 탐색하기위해 정렬

visited=[False]*(N+1)       #방문하지 않는 노드는 FALSE로 설정

def DFS(graph, v, visited):  
  visited[v]=True            #방문처리
  print(v, end=' ')          #방문한 노드 출력

  for i in graph[v]:          #현재 방문한 노드와 연결된 노드 탐색
    if not visited[i]:        #방문하지 않은 노드만 탐색
      DFS(graph, i, visited)

def BFS(graph, start, visited):
  queue=deque([start])
  visited[start]=True       #방문처리
  while queue:
    v=queue.popleft()       
    print(v, end=' ')       #현재 방문한 노드 출력
    for i in graph[v]:      #현재 노드와 연결된 노드들 탐색
      if not visited[i]:
        visited[i]=True
        queue.append(i)     #현재 노드와 연결된 노드들 큐에 추가


DFS(graph, V, visited)
print()
visited=[False]*(N+1)

BFS(graph, V, visited)
