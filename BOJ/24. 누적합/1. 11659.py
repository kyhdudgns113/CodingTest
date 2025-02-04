# 1 <= i <= j <= n
# 수열의 i 번째부터 j 번째의 합을 구한다
#
# nums[k] : (k + 1) 번째 수 (0 <= k < n)
# sums[k] : sum(nums[0] ~ nums[k])
# 구간합(i, j) = sums[j - 1] - sums[i - 1]

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
sums = [0 for i in range(n)]
sums[0] = nums[0]

for i in range(1, n):
  sums[i] = sums[i - 1] + nums[i]
  
for _ in range(m):
  i, j = map(int, input().split())
  result = sums[j - 1] - (sums[i - 2] if i > 1 else 0)
  print(result)