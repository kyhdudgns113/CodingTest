# n : 수열의 길이
# k : 연속된 숫자의 길이
# a[] : 입력 수열
#
# sums[i] : sum(a[0] ~ a[i])
#
# maxSum = max(
#   sum[k - 1] (0 번째 부터 (k - 1) 번째까지의 합 = k개)
#   sum[k] - sum[0]
#   sum[k + 1] - sum[2]
#     ...
#   sum[n - 1] - sum[n - k]
# )

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

sums = [0 for i in range(n)]
sums[0] = a[0]
for i in range(1, n):
  sums[i] = sums[i - 1] + a[i]
  
maxSum = sums[k - 1]
for i in range(k, n):
  maxSum = max(maxSum, sums[i] - sums[i - k])

print(maxSum)