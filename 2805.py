import sys
n, m=map(int, sys.stdin.readline().split())             # 파이썬 빠른 입력 방식
a=list(map(int, sys.stdin.readline().split()))

def cal(array, limit):                                  # limit = 절단기 높이
  copy=[0]*n                                            # copy배열 = 각 떡의 길이인 array배열에서 자르고 남은 떡의 길이
  for i in range(len(array)):
    if array[i] <= limit:                               # 절단기 높이보다 작은 떡은 0
      continue
    else:
      copy[i]=array[i]-limit                            # 절단기 높이보다 긴 떡은 절단기 높이만큼 자르고 남은 후의 길이 저장

  return sum(copy)

case=[]                                                 # 절단기 높이 중 최댓값을 얻기 위해 case에 가능한 절단기 높이 모두 저장

def binarysearch(target, start, end):                   # start = 0, end = 떡의 길이 중 가장 큰 떡의 길이, target = m
  while start<=end:
    mid=(start+end)//2
    result=cal(a, mid)
    
    if result<target:                                   # 자르고 남은 떡의 길이의 합이 손님이 요청한 길이보다 작은 경우
      end=mid-1                                         

    else:
      case.append(mid)                                  # 가능한 절단기 높이 case 리스트에 저장
      start=mid+1

  return None

binarysearch(m, 0, max(a))
print(max(case))                                      # 가능한 절단기 높이 중 최댓값 출력
