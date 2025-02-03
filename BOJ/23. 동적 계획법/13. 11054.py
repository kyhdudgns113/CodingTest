# 이 문제는 "11053 - 가장 긴 부분수열" 이랑 유사하게 풀 수 있다.
# a[] : 입력 수열
# bitonic[k] : "a[k]까지 증가하는 부분수열" + "a[k] 부터 감소하는 부분수열" - 1
#         = incArrLen[k] + decArrLen[k] - 1 (a[k] 가 중복된다)
#
# incArrLen 과 decArrLen 은 모두 n log n 으로 구현할 수 있긴 하다.
# 하지만 n = 1000 이므로 n^2 으로 풀어도 무방하여 그리 풀었다.
#
# incArrLen[k] = max( incArrLen[i] if a[i] < a[k], 0 <= i < k ) + 1
# decArrLen[k] = max( decArrLen[i] if a[i] < a[k], k < i < n ) + 1
#
# 출력값 = max (bitonic[i], 0 <= i < n)

import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

incArrLen = [0 for i in range(n)]
decArrLen = [0 for i in range(n)]

incArrLen[0] = 1
decArrLen[n - 1] = 1

for i in range(1, n):
  for j in range(i):
    if a[j] < a[i]:
      incArrLen[i] = max(incArrLen[i], incArrLen[j])
  incArrLen[i] += 1
  
  backIdx = n - 1 - i
  for j in range(i):
    nowIdx = n - 1 - j
    if a[backIdx] > a[nowIdx]:
      decArrLen[backIdx] = max(decArrLen[backIdx], decArrLen[nowIdx])
  decArrLen[backIdx] += 1
  
res = 0
for i in range(n):
  res = max(res, incArrLen[i] + decArrLen[i] - 1)
  
print(res)