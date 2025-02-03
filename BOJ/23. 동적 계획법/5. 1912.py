# a[n] : n 번째 입력
# sums[n] : n번째 입력까지의 합 = sum[n - 1] + a[n]
#
# a 번째부터 b 번째까지의 합 "구간합[b, a]" 은
# 구간합[b, a] = sum[b] - sum[a - 1] 로 나타낼 수 있다.
#
# 최대구간합[n - 1, 0] = 
#   max(
#     max(구간합[0, 0 ~ 0]),
#     max(구간합[1, 0 ~ 1]),
#     max(구간합[2, 0 ~ 2]),
#           ...
#     max(구간합[n - 1, 0 ~ n - 1])
#   )
#
# 임의의 b 에 대하여
#  구간합[b, a] = sum[b] - sum[a]
# 이 최대값을 가지려면
# 0 <= a < b 범위 내에서 sum[a] 가 가장 작아야 한다.
#
# 이는 반복문을 돌면서
# maxSum = max(maxSum, sum[a] - minVal)
# minVal = min(minVal, sum[a]) 로 갱신해준다.

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sums = [0 for i in range(n)]
sums[0] = arr[0]
for i in range(1, n):
  sums[i] = sums[i - 1] + arr[i]
  
maxSum = - 10 ** 9
minMinus = 0

for sumVal in sums:
  maxSum = max(maxSum, sumVal - minMinus)
  minMinus = min(minMinus, sumVal)

print(maxSum)