# n : 사다리의 갯수
# m : 뱀의 갯수
# ladders[] : (start, end) 사다리의 시작점 밑 끝점의 배열
# snakes[] : (start, end) 뱀의 시작점 밑 끝점의 배열
#
# 상황
#   1 에서 시작한다.
#   주사위를 1번 굴려서 이동한다.
#     만약 도착지점에 사다리나 뱀이 있다면 해당 요소의 end 로 이동한다.
#
# 구하는것
#   100 에 도착하기 위한 최소한의 주사위 횟수
#
# 풀이
#   bfs 로 구하면 된다.


from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ladders = [list(map(int, input().split())) for i in range(n)]
snakes = [list(map(int, input().split())) for i in range(m)]

dest = [0 for i in range(101)]

for ladder in ladders:
  start, end = ladder
  dest[start] = end

for snake in snakes:
  start, end = snake
  dest[start] = end
  
cnts = [1000 for i in range(101)]
nextQueue = deque()

nextQueue.append(1)
cnts[1] = 0

while len(nextQueue) > 0:
  elem = nextQueue.popleft()
  cnt = cnts[elem]
  
  for i in range(1, 7):
    if elem + i > 100:
      break
    if cnts[elem + i] < 1000:
      continue
    
    cnts[elem + i] = min(cnts[elem + i], cnt + 1)
    if dest[elem + i] > 0:
      cnts[dest[elem + i]] = min(cnts[dest[elem + i]], cnt + 1)
      nextQueue.append(dest[elem + i])
    else:
      nextQueue.append(elem + i)
      
print(cnts[100])
      