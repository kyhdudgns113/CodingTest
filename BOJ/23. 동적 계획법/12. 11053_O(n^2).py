# 이 코드는 가장 직관적인 O(n ^ 2) 로 짰다.
# n : 수열의 길이
# a[] : 수열
# maxLen[k] : a[k] 가 포함된 a[0]~a[k] 까지의 부분수열의 최대 길이
#
# maxLen[k] = 
#   max(
#     maxLen[k - 1] "if a[k - 1] < a[k]"  
#     maxLen[k - 2] "if a[k - 2] < a[k]"
#     ...
#     maxLen[0] "if a[0] < a[k]"
#   ) + 1
#
# 이를 단순하게 2중 반복문으로 짰다. 

import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

maxLen = [0 for i in range(n)]

for i in range(n):
  tempMax = 0
  for j in range(i):
    if a[j] < a[i]:
      tempMax = max(tempMax, maxLen[j])
  maxLen[i] = tempMax + 1
  
print(max(maxLen))

