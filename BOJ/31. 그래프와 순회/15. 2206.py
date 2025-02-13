# n, m : 지도의 세로, 가로 길이
# field[][] : 지도
#   0 = 길, 1 = 벽
#
# 상황
#   (0, 0) 부터 (n - 1, m - 1) 까지 이동한다.
#   벽은 하나까지 부술 수 있다.
#
# 구하는것
#   최단거리
#
# 풀이
#   기본적으로 한 칸씩 이동하면서 최단거리를 구할때는 bfs 를 쓸 수 있다.
#   isVisit[row][col][walled] 배열에 해당 상황에서의 최단거리를 기록한다.
#     walled : 0 이면 벽을 부순적 없다. 1 이면 벽을 부순적 있다.
#   bfs 반복문을 돌면서
#     벽을 부순적 없으면 벽을 새로 부수는 경우를 bfs 큐에 넣는다.
#     벽을 부순 여부랑 상관없이 길을 걷는 경우를 bfs 큐에 넣는다.

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(input().strip()) for i in range(n)]

isVisit = [[[0, 0] for i in range(m)] for j in range(n)]
nextVisit = deque()

nextVisit.append((0, 0, 0, 1))
isVisit[0][0][0] = 1

while len(nextVisit) > 0:
  row, col, walled, cnt = nextVisit.popleft()
  
  if walled == 0:
    if row > 0 and field[row - 1][col] == "1" and isVisit[row - 1][col][1] == 0:
      isVisit[row - 1][col][1] = cnt + 1
      nextVisit.append((row - 1, col, 1, cnt + 1))
    if col > 0 and field[row][col - 1] == "1" and isVisit[row][col - 1][1] == 0:
      isVisit[row][col - 1][1] = cnt + 1
      nextVisit.append((row, col - 1, 1, cnt + 1))
    if row < n - 1 and field[row + 1][col] == "1" and isVisit[row + 1][col][1] == 0:
      isVisit[row + 1][col][1] = cnt + 1
      nextVisit.append((row + 1, col, 1, cnt + 1))
    if col < m - 1 and field[row][col + 1] == "1" and isVisit[row][col + 1][1] == 0:
      isVisit[row][col + 1][1] = cnt + 1
      nextVisit.append((row, col + 1, 1, cnt + 1))
      
  if row > 0 and field[row - 1][col] == "0" and isVisit[row - 1][col][walled] == 0:
    isVisit[row - 1][col][walled] = cnt + 1
    nextVisit.append((row - 1, col, walled, cnt + 1))
  if col > 0 and field[row][col - 1] == "0" and isVisit[row][col - 1][walled] == 0:
    isVisit[row][col - 1][walled] = cnt + 1
    nextVisit.append((row, col - 1, walled, cnt + 1))
  if row < n - 1 and field[row + 1][col] == "0" and isVisit[row + 1][col][walled] == 0:
    isVisit[row + 1][col][walled] = cnt + 1
    nextVisit.append((row + 1, col, walled, cnt + 1))
  if col < m - 1 and field[row][col + 1] == "0" and isVisit[row][col + 1][walled] == 0:
    isVisit[row][col + 1][walled] = cnt + 1
    nextVisit.append((row, col + 1, walled, cnt + 1))
    
a, b = isVisit[n - 1][m - 1]

if a + b == 0:
  print(-1)
elif a == 0:
  print(b)
elif b == 0:
  print(a)
else:
  print(min(a, b))