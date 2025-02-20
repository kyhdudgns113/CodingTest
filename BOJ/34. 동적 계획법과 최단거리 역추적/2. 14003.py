# n : 수열의 갯수( n <= 1,000,000)
# a[] : 수열 (abs(a[i]) <= 1,000,000,000)
#
# 구하는것
#   가장 긴 부분 증가 수열
#   - 경우의 수가 여러개면 그 중 하나만 출력
#
# 풀이
#   tempArr : 임시 배열
#   prevIdxArr[i] : i 번쨰 수 이전에 a[i] 보다 작은 수중에서 가장 큰 수의 인덱스
#     a : 10 20 10 30 20 50 이면
#     prevIdx : -1 0 -1 1 2 4 이다.
#   0 <= i < n  에 대하여
#     a[i] 가 tempArr 에서 들어갈 인덱스를 찾는다.
#       해당 인덱스를 newIdx 라 하자.
#       temp[newIdx] 에 (a[i], i) 를 넣는다.
#         배열 길이를 초과하면 append 를 한다.
#       이 때 temp[newIdx - 1] 에 있는 원소는 다음과 같은 성질을 갖는다.
#         - a[i] 보다는 작다.
#         - a[i] 보다 작은 수 중에서 a[i] 와 가장 가까이 있다.
#           == a[i] 가 포함된 증가하는 부분수열에 꼭 들어간다.
#         - 따라서 prevIdxArr[i] 에 temp[newIdx - 1] 에 저장된
#           인덱스를 넣는다.
#         - 만약 newIdx == 0 이라면 a[i] 보다 작은수는 없으므로 -1 을 넣는다.
#
#   반복문을 다 돌았다면 다음을 수행한다.
#     tempArr 의 맨 뒤 원소부터 시작한다.
#     tempArr 에 저장된 a[i] 값을 resultArr 에 저장한다.
#     다음에 저장될 값은 tempArr 에 저장된 인덱스가 가리키는 값이다.
#     idx = prevIdx[tempArr[-1].idx] 를 넣는다.
#     a[idx] 를 resultArr 에 저장한다.
#     idx = prevIdx[idx] 를 넣는다.
#     idx = -1 이 될때까지 반복한다.
#
#   이후 resultArr 를 역순으로 출력하면 된다.
#
# 연산량
#   모든 a[] 요소에 대하여 : O(n)
#     tempArr 에 들어갈 자리를 찾는다. : O(log n)
#   = O(n log n)
#   = 대략 천만

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))

def binarySearch(val, arr, l, r):
  if l == r:
    if arr[l][0] < val:
      return l + 1
    else:
      return l
  if l + 1 == r:
    if arr[r][0] < val:
      return r + 1
    elif arr[l][0] < val <= arr[r][0]:
      return r
    else:
      return l
  mid = (l + r) // 2
  
  if arr[mid][0] <= val:
    return binarySearch(val, arr, mid, r)
  else:
    return binarySearch(val, arr, l, mid)
  
tempArr = [[a[0], 0]]
prevIdxArr = [-1 for i in range(n)]

for i in range(1, n):
  aa = a[i]
  newIdx = binarySearch(aa, tempArr, 0, len(tempArr) - 1)
  
  if newIdx == 0:
    prevIdxArr[i] = -1
  else:
    prevIdxArr[i] = tempArr[newIdx - 1][1]
    
  if newIdx == len(tempArr):
    tempArr.append([aa, i])
  else:
    tempArr[newIdx] = [aa, i]
    
resultArr = []

idx = tempArr[-1][1]

while idx >= 0:
  resultArr.append(a[idx])
  idx = prevIdxArr[idx]

l = len(resultArr)
print(l)
for i in range(l):
  output("%d " % resultArr[l - 1 - i])  