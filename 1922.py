import sys
input=sys.stdin.readline
n=int(input().rstrip())       # 정점 개수 입력
m=int(input().rstrip())       # 간선 개수 입력

def find_parent(parent, x):   # x가 있는 트리의 루트 노드를 parent[x]로 지정하고 반환하는 함수
  if parent[x]!=x:
    parent[x]=find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):       # a노드가 있는 트리와 b노드가 있는 트리를 합치는 함수
  a=find_parent(parent, a)            # a노드가 있는 트리의 루트 노드 찾기
  b=find_parent(parent, b)            # b노드가 있는 트리의 루트 노드 찾기
  if a<b:                             # a트리의 루트 노드의 값 < b트리의 로트 노드의 값 이면 
    parent[b]=a
  else:
    parent[a]=b

parent=[0]*(n+1)
for i in range(1, n+1):
  parent[i]=i                        # 처음엔 자기 자신이 자신의 부모 노드

edges=[]
for _ in range(m):
  a, b, cost=map(int, input().split())    # 연결된 두 노드와 비용 입력
  edges.append((cost, a, b))


edges.sort()        # 간선 비용에 따라 오름차순으로 정렬
result=0 


for edge in edges:
  cost, a, b=edge
  if find_parent(parent, a)!=find_parent(parent, b):    # 서로 다른 그룹이면 
    union_parent(parent, a, b)                          # 합치기
    result+=cost
      
print(result)
