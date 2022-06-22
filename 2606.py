n=int(input())
m=int(input())
count=0

graph=[[] for _ in range(n+1)]
ar=[]
for _ in range(m):
  ar.append(list(map(int, input().split())))  

for a, b in ar:
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()

visited=[False]*(n+1)
def dfs(graph, v, visited):
  global count
  visited[v]=True              # 방문 입력
  count+=1
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, 1, visited)
print(count-1)
