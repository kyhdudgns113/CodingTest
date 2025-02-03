#
# 입력쌍 [
#   [1, 8] [3, 9] [2, 2] [4, 1]
#   [6, 4] [10, 10] [9, 7] [7, 6]
# ] 은 다음과 같이 바꿀 수 있다.
#
# connectDic[from] : from 숫자가 연결되는 곳
#   connectDic[1] = 8
#   connectDic[3] = 9
#   connectDic[2] = 2
#   connectDic[4] = 1
#   connectDic[6] = 4
#   connectDic[10] = 10
#   connectDic[9] = 7
#   connectDic[7] = 6
#
# from 이 작은 순서대로 결과값을 저장하면 다음과 같다
#
# connectArr = [
#   8, 2, 9, 1, 4, 6, 7, 10
# ]
#
# 두 개의 선이 서로 꼬여있다는건 다음을 의미한다
#   => i < k && connectArr[i] > connectArr[k]
#
# 꼬인 선들을 없앤다는건 connectArr 에서 element 몇개를 제거하여
# connectArr 를 "증가하는 수열" 로 만든다는 것이다.
#
# 선들을 최소한으로 없앤다는건 element 를 최소한으로 제거한다는 뜻이고,
# connectArr 의 증가하는 부분수열의 깅이를 최대로 한다는 의미다.
#
# 없애는 전깃줄 최소 개수 = 전체 갯수 - 최대 증가하는 부분수열 길이
#
# 전체 갯수는 n 으로 고정이며, 최대 증가하는 부분수열의 길이는
# n^2, n log n 으로 구현할 수 있다.
#
# n = 100 이므로 구현이 빠른 n^2 을 택해도 된다.

import sys

input = sys.stdin.readline

n = int(input())

connectDic = {}

for _ in range(n):
  a, b = map(int, input().split())
  connectDic[a] = b
  
connectArr = []
keyArr = []

for key in connectDic.keys():
  keyArr.append(key)
keyArr.sort()

for key in keyArr:
  connectArr.append(connectDic[key])
  
incArrLen = [1 for i in range(n)]
for i in range(n):
  for j in range(i):
    if connectArr[j] < connectArr[i]:
      incArrLen[i] = max(incArrLen[i], incArrLen[j] + 1)
      
print(n - max(incArrLen))