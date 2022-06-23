import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):

  if x<0 or x>=w or y<0 or y>=h:
    return False

  if graph[y][x]==1:
    graph[y][x]=0
    dfs(x, y+1)          # 상
    dfs(x, y-1)          # 하
    dfs(x+1, y)          # 우
    dfs(x-1, y)          # 좌
    dfs(x+1, y-1)        # 우대각상
    dfs(x-1, y-1)        # 좌대각상
    dfs(x+1, y+1)        # 우대각하
    dfs(x-1, y+1)        # 좌대각하
    return True

  return False
  
while True:
  count=0                               # 섬의 개수

  w, h = map(int, input().split())      #지도 너비, 높이 입력

  if w==0 and h==0:             # 지도 너비, 높이 0, 0 입력시 프로그램 종료
    break

  graph=[]
  for _ in range(h):            # 지도 입력
    graph.append(list(map(int, 
    input().split())))

  for i in range(h):            # 모든 노드마다 깊이우선탐색 
    for j in range(w):
      if dfs(j, i)==True:
        count+=1

  print(count)

