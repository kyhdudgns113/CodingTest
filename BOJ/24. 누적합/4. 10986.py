# n : 수열의 길이
# m : 상수수
# a[] : 수열
#
# 구하고자 하는것 : 수열의 특정구간이 m 으로 나누어 떨어지는 경우의 수
#
# sums[k] = sum(a[0], a[1] ... a[k]) % m (m 으로 나눈 나머지를 저장한다)
# mods[x] : sums[i] = x 인 경우의 수
#
# m 으로 나누어 떨어지는 경우의 수
#   0 <= mod < m 에 대하여
#     - sums[r] - sums[l] = 0 (r > l) 이 되는 경우의 수
#     Case 1. mod == 0
#       sums[r] - sums[l] 뿐만 아니라
#       sums[r] - 0 인 경우도 세줘야 한다.
#       따라서 이 경우의 수는
#           mods[0] 개 중에서 2개 고르는 경우의 수
#         + mods[0]
#         = mods[0] * (mods[0] + 1) // 2
#
#     Case 2. mod != 0
#       mods[mod] 개 중에서 2개를 고르는 경우의 수를 세면 된다
#       = mods[mod] * (mods[mod] - 1) // 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
  
sums = [0 for i in range(n)]
mods = [0 for i in range(m)]

sums[0] = a[0] % m
mods[sums[0]] = 1

for i in range(1, n):
  sums[i] = (sums[i - 1] + a[i]) % m
  mods[sums[i]] += 1
  
res = 0
res += mods[0] * (mods[0] + 1) // 2
for i in range(1, m):
  res += mods[i] * (mods[i] - 1) // 2
  
print(res)
  
