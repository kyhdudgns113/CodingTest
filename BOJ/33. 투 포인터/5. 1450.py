#
# n : 물건의 개수 (n <= 30)
# c : 최대 중량 (c <= 1,000,000,000)
# weights[] : 물건들의 중량 (weights[i] <= 1,000,000,000)
#
# 구하는것
#   물건을 드는 경우의 수
#
# 풀이
#   분할정복을 쓴다.
#   getPartResult(l, r)
#     weight[l] 부터 weights[r] 까지의 물건중에서
#     무게 c 를 넘지 않게 드는 경우의 수
#   1. 물건 배열을 두 그룹으로 나눈다. (weights[l:mid+1], weights[mid+1:r])
#   2. 각 그룹에 대하여 그룹내의 물건들 중에서 짊어지는 경우의 수를 구한다.
#       getPartResult(l, mid), getPartResult(mid + 1, r)
#   3. 그룹끼리 교차하여 물건을 드는 경우의 수를 구한다.
#    
# 연산량
#   1. O(1)
#   2. 2*O(f(n / 2))
#   3
#     왼쪽 배열의 원소 갯수의 최대값
#       = 15개의 물건을 드는 경우의 수
#       = 약 320만
#     c - 원소값 을 배치할 인덱스를 찾는 경우
#       = log (오른 배연의 원소 갯수의 최대값)
#       = log (320만)
#     둘이 곱하면 대략 1500만이다.

from itertools import combinations
import sys

input = sys.stdin.readline

n, c = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

# arr 에서 val 이 들어갈 위치를 찾는다.
# 같은 원소가 있으면 그 원소의 다음 인덱스를 리턴한다.
# val 이 제일 크면 arr 의 길이를 리턴한다.
def binarySearch(val, arr, l, r):
  if l == r:
    if val >= arr[l]:
      return l + 1
    else:
      return l
  if l + 1 == r:
    if val >= arr[r]:
      return r + 1
    elif arr[l] <= val:
      return r
    else:
      return l
    
  mid = (l + r) // 2
  
  if val < arr[mid]:
    return binarySearch(val, arr, l, mid - 1)
  else:
    return binarySearch(val, arr, mid, r)

def getSortedCombination(arr):
  l = len(arr)
  result = []
  for i in range(1, l + 1):
    for partArr in combinations(arr, i):
      result.append(sum(partArr))
  result.sort()
  return result

def getPartResult(l, r):
  global n, c
  if l == r:
    if weights[l] <= c:
      return 1
    else:
      return 0
  if l + 1 == r:
    if weights[l] + weights[r] <= c:
      return 3
    elif weights[l] <= c and weights[r] <= c:
      return 2
    elif weights[l] <= c:
      return 1
    else:
      return 0
    
  mid = (l + r) // 2
  
  leftArr = getSortedCombination(weights[l:mid + 1])
  rightArr = getSortedCombination(weights[mid+1:r+1])
  
  leftResult = getPartResult(l, mid)
  rightResult = getPartResult(mid + 1, r)
  
  entireResult = 0
  lenRight = len(rightArr)
  for val in leftArr:
    entireResult += binarySearch(c - val, rightArr, 0, lenRight - 1)
    
  return leftResult + entireResult + rightResult

print(getPartResult(0, n - 1) + 1)
  
