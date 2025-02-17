#
# n : 수열 원소의 갯수 (n <= 100,000)
# s : 기준이 되는 수 (s <= 100,000,000)
# arr[] : 수열 (0 < arr[i] <= 10000)
#
# 구하는것
#   arr 에서 연속된 숫자의 합 중에서 s 이상인 수열중
#   길이가 가장 짧은것
#
# 풀이
#   l = 0, r = 0, tempSum = arr[0] (l 부터 r 까지의 합)
#   다음 반복문을 돈다.
#     - tempSum >= s 면 최소길이 갱신
#
#     - tempSum <= s 일 때
#       r 을 늘릴 수 있으면 1 늘린다.
#         - tempSum 을 늘려줘야 한다.
#       그렇지 못하면 l 을 1 늘린다.
#     - tempSum > s 일 때
#       l 을 1 늘려준다.
#         - tempSum 을 줄여야 한다.

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

minLen = n + 1
l = 0
r = 0
tempSum = arr[0]

while l <= n - 1:
  if tempSum >= s:
    minLen = min(minLen, r - l + 1)
    
  if tempSum <= s:
    if r < n - 1:
      r += 1
      tempSum += arr[r]
    else:
      tempSum -= arr[l]
      l += 1
  else:
    tempSum -= arr[l]
    l += 1
    
if minLen > n:
  print(0)
else:
  print(minLen)
