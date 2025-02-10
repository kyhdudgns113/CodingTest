# n : 프로세스의 수 (n <= 100)
# m : 확보해야 할 최소의 메모리량 (m <= 10,000,000)
# mem[] : 각 프로세스마다 점유중인 메모리 (mem[i] <= 10,000,000)
# cost[] : 각 프로세스마다 종료할때 소모되는 코스트 (cost[i] <= 100)
#
# 상황
#   프로세스를 적절히 종료하여 m 만큼의 메모리를 확보해야 한다.
#   각 프로세스는 강제종료하면 코스트가 발생한다.
#
# 구하는것
#   m 이상의 메모리를 확보하는데 필요한 최소한의 코스트
#
# 첫 번째 풀이 아이디어 (기각됨 : 연산량 초과)
#   0 <= i <= 100 (모든 프로세스에 대하여)
#     0 <= j <= 10,000,000 (모든 메모리량에 대하여)
#       result[i][j + mem[i]] = result[i - 1][j] + cost[i]
#
#   연산량이 100 * 10,000,000 = 10억 > 1억
#   시간초과가 난다.
#
# 두 번째 풀이 아이디어
#   메모리량에 대해서 연산하는것이 아닌 코스트량에 대하여 연산을 한다
#     - 각 코스트별로 확보할 수 있는 최대 메모리량을 구한다.
#     - 이후 cost=0 부터 시작하여 확보 가능한 메모리량이 m 이상이면 멈춘다.
#     - 그러면 메모리 m 을 확보하기 위한 최소한의 코스트를 구할 수 있다.
#   연산량
#     0 <= i <= 100
#       0 <= j <= 10,000 (프로세스 100개, 개당 최대 코스트 100)
#         result[i][j + cost[i]] = result[i - 1][j] + mem[i]
#   = 100 * 10,000 = 1,000,000

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memArr = list(map(int, input().split()))
costArr = list(map(int, input().split()))

maxMem = [[0 for i in range(10001)] for j in range(n)]

for i in range(n):
  
  maxMem[i][costArr[i]] = max(maxMem[i][costArr[i]], memArr[i])
  if i > 0:
    for j in range(10001):
      if maxMem[i - 1][j] > 0:
        maxMem[i][j] = max(maxMem[i][j], maxMem[i - 1][j])
        if j + costArr[i] <= 10000:
          maxMem[i][j + costArr[i]] = max(
            maxMem[i][j + costArr[i]],
            maxMem[i - 1][j] + memArr[i]
          )

for cost in range(10001):
  if maxMem[n - 1][cost] >= m:
    print(cost)
    break