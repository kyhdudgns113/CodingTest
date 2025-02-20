# n : 이진트리 점의 갯수 (n <= 100,000)
# lvr[] : 이진트리를 lvr 로 순회한 결과
# lrv[] : 이진트리를 lrv 로 순회한 결과
#
# 상황
#   트리는 1부터 n 까지 숫자로 중복없이 이루어져있다.
#
# 구하는것
#   vlr 로 순회했을때의 결과
#
# 풀이
#   주어진 범위의 lvr 과 lrv 에서
#     lrv 의 마지막 원소가 주어진 범위에서 루트인 v 이다.
#     lvr 에서 v 가 들어가있는 인덱스를 찾는다.
#     해당 인덱스를 이용하여 lvr 에서 l 의 개수를 찾는다.
#     l 의 갯수를 이용하여 lrv 에서 l 에 해당하는 범위를 찾는다.
#   v 를 출력한다.
#   l 에 해당하는 범위에 대해서 vlr 을 구한다.
#   r 에 해당하는 범위에 대해서 vlr 을 구한다.
#
# 연산량
#   1. 각 v 값에 대하여 lvr 의 위치를 기록한다 : O(n)
#   2. 재귀함수로 vlr 을 구한다 : O(n)
#   1 + 2 = O(n) = 약 수십만만

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

lvr = list(map(int, input().split()))
lrv = list(map(int, input().split()))

vInLVRArr = [0 for i in range(n + 1)]
for i in range(n):
  vInLVRArr[lvr[i]] = i

def getVLR(lvrStart, lvrEnd, lrvStart, lrvEnd):
  
  if lvrStart > lvrEnd:
    return
  
  vInLRV = lrvEnd
  vInLVR = vInLVRArr[lrv[vInLRV]]
  numLeft = vInLVR - lvrStart
  numRight = lvrEnd - vInLVR
  lastLIdxInLRV = lrvStart + numLeft - 1
  
  output("%d " % lvr[vInLVR])
  if numLeft > 0:
    getVLR(lvrStart, vInLVR - 1, lrvStart, lastLIdxInLRV)
  if numRight > 0:
    getVLR(vInLVR + 1, lvrEnd, lastLIdxInLRV + 1, lrvEnd - 1)
  
getVLR(0, n - 1, 0, n - 1)