# 해당 문제는 백준에서 pypy3으로 실행해야 시간 초과가 뜨지 않습니다. Python3으로 실행하면 시간초과가 뜹니다.
from collections import deque

count=0         # 연결 요소 개수

n, m = map(int, input().split())    # 정점개수, 간선개수 입력

visited=[False]*(n+1)

graph=[[] for _ in range(n+1)]

for _ in range(m):
  x, y=map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

#너비우선탐색
def bfs(graph, start, visited):
  queue=deque([start])
  visited[start]=True           # 방문처리
  while queue:
    v=queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True       # 방문 처리
        
for i in range(1, n+1):
  if not visited[i]:
    count+=1
    bfs(graph, i, visited)    # 한 개의 연결 요소 중 어떠 노드를 깊이우선탐색하면 연결된 모든 노드도 방문처리됨. 
                              # 그러므로 모든 노드에 대해 깊이우선탐색을 해도 상관없음.
print(count)
