# n : 집의 갯수
# c : 공유기의 갯수
# houses[] : 일직선상의 집의 좌표
#
# 상황 : 집에 공유기를 적절히 배치한다.
# 구하는것
#   - 가장 가까운 공유기 사이의 거리의 최대값
#
# 풀이
#   - houses 를 오름차순으로 정렬한다.
#   - start=0 부터 end=10^9 의 범위에서 다음을 수행한다.
#     - mid = (start + end) // 2 라고 하자.
#     Case 1.
#       - 공유기 사이의 거리를 mid 이상으로 c 개 배치할 수 있을때
#       - 거리는 mid 일수도 있고, mid 보다 클 수도 있다.
#       - 범위를 (mid, end) 로 바꾸고 다시 연산한다.
#     Case 2.
#       - 공유기 사이의 거리가 mid 면 c개를 배치할 수 없을때
#       - 거리는 mid 보단 작아야 한다.
#       - 범위를 (start, mid - 1) 로 바꾸고 연산한다.
#
#   - canSetByDistance(distance)
#     - 공유기 사이의 거리를 distance 이상으로 유지하면서
#     - 공유기를 c 개 이상 설치할 수 있는지를 리턴한다.
#       1. houses[0] 에 하나를 설치하며 cnt = 1 로 설정한다.
#       2. lastHouse:마지막에 설치한집 = house[0] 으로 한다.
#       3. 1 <= i < n 에 대하여
#         lastHouse 로부터 거리가 distance 이상이면
#           - 공유기를 설치하고 cnt 를 1 늘린다.
#           - lastHouse 를 현재 집 houses[i] 로 한다.
#       4. cnt 가 c 이상이면 True 를 리턴한다.
#       5. 아니면 False 를 리턴한다.

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

n, c = map(int, input().split())
houses = list(int(input()) for i in range(n))

houses.sort()

# 공유기 사이의 거리를 distance 이상으로 유지하면서
# c 개를 설치할 수 있는지를 리턴한다.
def canSetByDistance(distance):
  global n, c
  cnt = 1
  lastHouse = houses[0]
  
  for i in range(1, n):
    if houses[i] - lastHouse >= distance:
      cnt += 1
      lastHouse = houses[i]
    if cnt == c:
      return True
  return False 

def findDistance(start, end):
  if start == end:
    return start
  if start + 1 == end:
    if canSetByDistance(end):
      return end
    return start
  
  mid = (start + end) // 2
  
  if canSetByDistance(mid):
    return findDistance(mid, end)
  else:
    return findDistance(start, mid - 1)
    
print(findDistance(1, (10 ** 9)//c + 1))
  
