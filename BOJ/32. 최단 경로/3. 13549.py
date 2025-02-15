# n : 시작 자연수
# k : 도착 자연수 (n, k <= 100,000)
# 
# 상황
#   x 에서 1초뒤에 x + 1 이나 x - 1 로 갈 수 있다.
#   x 에서 0초뒤에 2x 로 갈 수 있다.
#
# 구하는것
#   n 에서 k 로 가는 최단시간
#
# 풀이
#   bfs 로 풀면 된다.
#     x 에서 2x, x + 1, x - 1 로 가는 경우에 대해서 bfs 를 한다.
#     2x 를 x + 1 이나 x - 1 보다 먼저 해야 한다.
#     이유는 하단에 설명했다.

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

cnts = [400000 for i in range(400001)]

nextVisit = deque()
nextVisit.append(n)
cnts[n] = 0

while len(nextVisit) > 0:
  now = nextVisit.popleft()
  
  # 2*now == now + 1 일 수 있다.
  # 이 때 cnts[2*now] 에는 cnts[now] + 1 이 아닌
  # cnts[now] 가 들어가야 한다.
  # 따라서 2*now 인 경우를 먼저 확인한다.
  if now < 200000 and cnts[2*now] == 400000:
    cnts[2*now] = cnts[now]
    nextVisit.append(2 * now)
  if now > 0 and cnts[now - 1] == 400000:
    cnts[now - 1] = cnts[now] + 1
    nextVisit.append(now - 1)
  if now < 400000 and cnts[now + 1] == 400000:
    cnts[now + 1] = cnts[now] + 1
    nextVisit.append(now + 1)
    
print(cnts[k])