# bottom-up 방식

n=int(input())

d=[0]*1000001                                     # index에 해당하는 수에 도달하기까지의 연산 횟수

for i in range(1, n):
  if 3*i <= n:                                    # 3배
    comp=1+d[i]
    if d[3*i]!=0:                                 # 이미 다른 값이 저장되어있다면 
      d[3*i]=min(d[3*i], comp)                    # 새로운 값과 기존 값 중 최소값을 연산 횟수로 저장
    else:
      d[3*i]=comp                                 # 저장되어있는 값이 없다면 새로운 값 그대로 저장

  if 2*i <= n:                                    # 2배
    comp=1+d[i]
    if d[2*i]!=0:
      d[2*i]=min(d[2*i], comp)
    else:
      d[2*i]=comp

  if 1+i <= n:                                    # 더하기 1
    comp=1+d[i]
    if d[1+i]!=0:
      d[1+i]=min(d[1+i], comp)
    else:
      d[1+i]=comp

print(d[n])                                       # n에 도달하기까지의 연산 횟수
