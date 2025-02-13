# m : 상자의 가로 길이
# n : 상자의 세로 길이
# h : 상자를 위로 쌓은 개수
# tomatos[][][] : 익은 토마토는 1, 안 익은 토마토는 0, 빈칸은 -1
#
# 상황
#   익은 토마토는 다음날에 1칸 범위에 있는 토마토들을 익게 만든다.
#
# 구하는것
#   상자안의 토마토가 모두 익는데까지 걸리는 시간
#   모두 익지 않는다면 -1
#
# 풀이
#   bfs 로 하면 된다.

from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())
tomatos = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]

nextQueue = deque()

for height in range(h):
  for row in range(n):
    for col in range(m):
      if tomatos[height][row][col] == 1:
        nextQueue.append([height, row, col])
        
        
while len(nextQueue) > 0:
  elem = nextQueue.popleft()
  
  height = elem[0]
  row = elem[1]
  col = elem[2]
  cnt = tomatos[height][row][col]
  
  if height > 0 and tomatos[height - 1][row][col] == 0:
    tomatos[height - 1][row][col] = cnt + 1
    nextQueue.append([height - 1, row, col])
  if height < h - 1 and tomatos[height + 1][row][col] == 0:
    tomatos[height + 1][row][col] = cnt + 1
    nextQueue.append([height + 1, row, col])
  if row > 0 and tomatos[height][row - 1][col] == 0:
    tomatos[height][row - 1][col] = cnt + 1
    nextQueue.append([height, row - 1, col])
  if row < n - 1 and tomatos[height][row + 1][col] == 0:
    tomatos[height][row + 1][col] = cnt + 1
    nextQueue.append([height, row + 1, col])
  if col > 0 and tomatos[height][row][col - 1] == 0:
    tomatos[height][row][col - 1] = cnt + 1
    nextQueue.append([height, row, col - 1])
  if col < m - 1 and tomatos[height][row][col + 1] == 0:
    tomatos[height][row][col + 1] = cnt + 1
    nextQueue.append([height, row, col + 1])
  
result = 0
  
for height in range(h):
  for row in range(n):
    for col in range(m):
      if tomatos[height][row][col] == 0:
        print(-1)
        exit()
      else:
        result = max(result, tomatos[height][row][col] - 1)
        
print(result)
    