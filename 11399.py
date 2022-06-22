N=int(input())
a=list(map(int, input().split()))
a.sort()

total=0
for i in a:
  total += i*N
  N=N-1

print(total)
