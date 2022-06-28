import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n, e=map(int, input().split())            # 정점, 간선 개수 입력
k=int(input())                            # 시작점 입력

graph=[[] for _ in range(n+1)]            # 간선으로 연결된 두 정점 사이의 거리 입력
distance=[INF]*(n+1)                      # 시작점에서 각 정점들까지의 최단 거리

for _ in range(e):
  u, v, w=map(int, input().split())       # u정점에서 v정점까지의 w거리 또는 가중치
  graph[u].append((v, w))

def dijkstra(start):
  distance[start]=0                       # 시작점 최단거리 = 0
  q=[]
  heapq.heappush(q, (0, start))

  while q:
    dist, now=heapq.heappop(q)
    if distance[now]<dist:                # 시작점에서 now지점까지의 새로 입력된 거리가 최단거리보다 클 때 무시
      continue

    for i in graph[now]:                  
      cost=dist+i[1]                      # 시작점에서 now지점까지의 거리 + now지점에서 i지점까지의 거리 = 시작점에서 i 지점까지의 거리
      if cost<distance[i[0]]:             # 입력된 시작점에서 i지점까지의 거리가 기존 최단거리보다 작을 때
        distance[i[0]]=cost               # 최단거리 갱신
        heapq.heappush(q, (cost, i[0]))


dijkstra(k)

for i in range(1, n+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])
