N, K = map(int, input().split())
kind=[]
count=0

for _ in range(N):
  kind.append(int(input()))
  
kind.sort(reverse=True)
for i in range(N):
  count+=(K//kind[i])
  K=K%kind[i]

print(count)
