#
# n : 일직선상에 있는 도시의 갯수
# distToNext[i] : i 번째 도시에서 i + 1 번째 도시까지의 거리
# prices[i] : i 번째 도시에서의 기름값
#
# result : 0번째 도시부터 n - 1 번째 도시시까지 이동할때 기름값의 최소값
#
# 기름값이 싼 곳일수록 많이 넣어야 한다.
#
# 0 번째 도시에서는 어쩔 수 없이 기름을 넣어야 한다.
# 0 번째 도시보다 기름값이 싼 가장 가까운 도시까지는 갈 수 있어야 한다.
# 딱 이정도로만 넣는다.
#
# 기름값 = prices[0] 으로 하고
# 기름값 > prices[i] 가 될 때 까지 해당 기름값으로 이동을 하면 된다.
#

import sys

input = sys.stdin.readline

n = int(input())
distToNext = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
minPrice = 10 ** 9 + 1

for i in range(n - 1):
  minPrice = min(minPrice, prices[i])
  result += minPrice * distToNext[i]

print(result)