#
# n : 시작하는 숫자
# k : 끝나는 숫자 (n, k <= 100,000)
#
# 상황
#   숫자는 다음 셋 중 하나의 연산을 할 수 있다.
#   1. 1을 뺀다.
#   2. 1을 더한다.
#   3. 2를 곱한다.
#
# 구하는것
#   n 에서 k 로 갈 때 가장 빠르게 가는 횟수
#
# 풀이
#   dfs 로는 시간 내에 풀 수 없다.
#     최단거리를 구하려면 n 에서 k 로 가는 모든 경우의 수를 다 확인하게 된다.
#   bfs 로는 가능하다.
#     한 숫자는 한 번만 방문하게 할 수 있다.
#     더하기, 빼기, 곱하기에 대하여 bfs 를 수행하면 된다.

from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, k = map(int, input().split())

isVisit = [0 for i in range(200001)]
nextQueue = deque()

def bfs(now, nowTime):
  isVisit[now] = nowTime
  
  if now > 0 and isVisit[now - 1] == 0:
    nextQueue.append({'val': now - 1, 'time': nowTime + 1})
  if now < 200000 and isVisit[now + 1] == 0:
    nextQueue.append({'val': now + 1, 'time': nowTime + 1})
  if now < 100000 and isVisit[2*now] == 0:
    nextQueue.append({'val': 2*now, 'time': nowTime + 1})
  
  while len(nextQueue) > 0:
    elem = nextQueue.popleft()
    if isVisit[elem['val']] == 0:
      return bfs(elem['val'], elem['time'])
  
  return 0

bfs(n, 1)

print(isVisit[k] - 1)