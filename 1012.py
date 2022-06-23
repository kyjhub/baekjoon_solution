import sys
sys.setrecursionlimit(10**6)

t=int(input())
# 1회 탐색시 배추 있는 칸의 개수
count=0          
result=0      # 배추가 모여있는 영역의 개수
def dfs(x, y):
  global count
  # 표의 범위를 벗어난 곳 탐색시 종료
  if x<0 or x>=m or y<0 or y>=n:
   return False

  if graph[y][x]==1:  # 배추가 있는 곳
   count+=1          
   graph[y][x]=0     # 방문 처리
   dfs(x+1, y)       # 상하좌우 방문
   dfs(x-1, y)
   dfs(x, y+1)
   dfs(x, y-1)

  # 배추가 없는 곳 탐색시 종료
  elif graph[y][x]==0:  
    return False

  
for _ in range(t):
  result=0
  m, n, k=map(int, input().split())

  graph=[[0]*m for _ in range(n)]
  
  for _ in range(k):
    x, y=map(int, input().split())
    graph[y][x]=1

  # 모든 노드 탐색
  for i in range(n):
    for j in range(m):
      count=0
      dfs(j, i)
      if count>0:   # 1회 탐색시 배추가 한칸이라도 있었다면 배추영역 수인 result에 +1
        result+=1
  print(result)
