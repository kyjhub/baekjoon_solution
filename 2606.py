n=int(input())
m=int(input())
count=0

graph=[[] for _ in range(n+1)]
ar=[]
for _ in range(m):
  ar.append(list(map(int, input().split())))        # 입력

for a, b in ar:
  graph[a].append(b)                                # a노드와 연결된 노드를 a번째 리스트에 입력
  graph[b].append(a)                                # b노드와 연결된 노드를 b번째 리스트에 입력

for i in range(n+1):
  graph[i].sort()                                   # i노드와 연결된 노드들을 오름차순으로 정렬

visited=[False]*(n+1)
def dfs(graph, v, visited):                         # 깊이우선탐색
  global count
  visited[v]=True                                   # 방문 입력
  count+=1
  for i in graph[v]:                                # v노드와 연결된 노드들 중
    if not visited[i]:                              # 아직 방문하지 않은 노드들로 
      dfs(graph, i, visited)                        # 다시 깊이우선탐색

dfs(graph, 1, visited)
print(count-1)              # 1번 컴퓨터에 의해 감염된 컴퓨터 수 이므로 count에는 1번 컴퓨터도 포함되어 있으므로 1을 빼준다.
