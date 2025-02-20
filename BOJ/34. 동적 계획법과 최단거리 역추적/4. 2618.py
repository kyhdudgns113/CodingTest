#
# n : 정사각형 지도의 크기 (n <= 1,000)
# w : 사건의 갯수 (w <= 1,000)
#
# accidents[] : (row, col) 로 구성된 사건의 발생장소의 배열
#               발생한 시간순서대로 배열된다.
#
# 상황
#   1번 경찰차는 1, 1 에 있다.
#   2번 경찰차는 n, n 에 있다.
#   사건이 발생하면 1번 경찰차나 2번 경찰차가 이동한다.
#   이동거리를 기록한다.
#
# 구하는것
#   사건들을 처리하고나서 가장 적은 이동거리를 구한다.
#   사건마다 어느 경찰차가 이동했는지를 기록한다.
#
# 풀이
#   cost[a][b] : 1번이 마지막으로 a 를 해결, 2번이 마지막으로 b 를 해결했을때 최단거리
#
#   cost[a][b] 를 알고 있을때
#     a > b:
#       cost[a + 1][b] = min(자기자신, cost[a][b] + dist(a, a + 1))
#       cost[a][a + 1] = min(자기자신, cost[a][b] + dist(b, a + 1))
#       이렇게 2개를 구할 수 있다.
#
#   이를 각 사건에 대하여 연산을 할 수 있다.
#
#   lastRowCol[a][b] : 1번차가 마지막에 사건 a 를 처리하고, 2번차가 마지막에 사건 b 를 처리했을때
#                     이 상황이 있기 바로 직전에 1번차와 2번차가 처리한 사건건
#
#   각 사건 workIdx 에 대하여 (i <= workIdx)
#     1. cost[workIdx][i] 에서 1번차를 보내서 cost[workIdx + 1][i] 를 구할 수 있다.
#     2. cost[i][workIdx] 에서 2번차를 보내서 cost[i][workIdx + 1] 를 구할 수 있다.
#     3. cost[i][workIdx] 에서 1번차를 보내서 cost[workIdx + 1][workIdx] 를 구할 수 있다.
#     4. cost[workIdx][i] 에서 2번차를 보내서 cost[workIdx][workIdx + 1] 를 구할 수 있다.
#   만약 각각 최소값이 갱신된다면 lastRowCol를 갱신한다.
#     1번 케이스에서는 lastRowCol[workIdx + 1][i] = [workIdx, i] 가 된다.
#     2번 케이스에서는 lastRowCol[i][workIdx + 1] = [i, workIdx] 가 된다.
#
#   위 반복문을 돌았으면 cost[w - 1][i] 와 cost[i][w - 1] 중에서 최소값을 찾는다.
#     최소값일때 1번차와 2번차의 위치 (row, col) 도 기록한다.
#
#   nextRow, nextCol = lastRowCol[row][col] 을 이용하여 어느 차가 이동했는지를 역추적 한다.
#     nextRow == row 면 1번차는 그대로 있었다는 뜻이다 => 2번차가 이동했다고 기록
#     nextCol == col 이면 2번차는 그대로 있었다는 뜻이다 => 1번차가 이동했다고 기록
#
#   위 기록을 역순으로 출력한다.
#
# 연산량
#   모든 사건의 개수에 대하여 : O(w)
#   이전 사건들을 4번정도 계산한다. : O(w)
#   = O(w) * O(w)
#   = O(w^2)
#   = 백만
#

import sys

input = sys.stdin.readline

n = int(input())
w = int(input())

accidents = [list(map(int, input().split())) for i in range(w)]
costByLastWork = [[10 ** 9 for i in range(w + 1)] for j in range(w + 1)]

#######################################################################
#                                                                     #
# lastRowCol[a][b] : 1번 경찰차가 a 에 있고, 2 번 경찰차가 b 에 있을때   #
#                   이전에 각 경찰차가 위치하던 곳                      #
#                   a, b 는 accidents 의 인덱스이다.                   #
#######################################################################
lastRowCol = [[[-1, -1] for i in range(w + 1)] for j in range(w + 1)]

# bef 에서 aft 로 이동할때의 이동거리
# is11 이 True 면 1번 경찰차가 이동한것. False 면 2번 경찰차.
def getDistance(bef, aft, is11):
  global n
  r0, c0 = accidents[bef]
  rz, cz = accidents[aft]
  
  if bef == -1:
    if is11 == True:
      r0, c0 = 1, 1
    else:
      r0, c0 = n, n
      
  return abs(rz - r0) + abs(cz - c0)

costByLastWork[-1][-1] = 0
costByLastWork[0][-1] = getDistance(-1, 0, True)
costByLastWork[-1][0] = getDistance(-1, 0, False)
costByLastWork[0][0] = getDistance(-1, 0, True) + getDistance(-1, 0, False)

lastRowCol[0][0] = [-1, 0]

for workIdx in range(w - 1):
  for i in range(-1, workIdx + 1):
    # (workIdx, i) 에서 1번 경찰차가 이동하는 경우
    tempVal = costByLastWork[workIdx][i] + getDistance(workIdx, workIdx + 1, True)
    if costByLastWork[workIdx + 1][i] > tempVal:
      costByLastWork[workIdx + 1][i] = tempVal
      lastRowCol[workIdx + 1][i] = [workIdx, i]
      
    # (i, workIdx) 에서 2번 경찰차가 이동하는 경우
    tempVal = costByLastWork[i][workIdx] + getDistance(workIdx, workIdx + 1, False)
    if costByLastWork[i][workIdx + 1] > tempVal:
      costByLastWork[i][workIdx + 1] = tempVal
      lastRowCol[i][workIdx + 1] = [i, workIdx]
      
    # (i, workIdx) 에서 1번 경찰차가 이동하는 경우
    tempVal = costByLastWork[i][workIdx] + getDistance(i, workIdx + 1, True)
    if costByLastWork[workIdx + 1][workIdx] > tempVal:
      costByLastWork[workIdx + 1][workIdx] = tempVal
      lastRowCol[workIdx + 1][workIdx] = [i, workIdx]
    
    # (workIdx, i) 에서 2번 경찰차가 이동하는 경우
    tempVal = costByLastWork[workIdx][i] + getDistance(i, workIdx + 1, False)
    if costByLastWork[workIdx][workIdx + 1] > tempVal:
      costByLastWork[workIdx][workIdx + 1] = tempVal
      lastRowCol[workIdx][workIdx + 1] = [workIdx, i]
    
minResult = 10 ** 9
row = 0
col = 0
for i in range(-1, w):
  if minResult > costByLastWork[w - 1][i]:
    minResult = costByLastWork[w - 1][i]
    row, col = w - 1, i
  if minResult > costByLastWork[i][w - 1]:
    minResult = costByLastWork[i][w - 1]
    row, col = i, w - 1
    
resultArr = []

# 최단거리일때 1번 경찰차와 2번 경찰차의 위치에서 시작한다.
# 이들이 어디에서 왔는지를 역추적 한다.
while row != -1 or col != -1:
  nextRow, nextCol = lastRowCol[row][col]
  if nextRow == row:
    resultArr.append(2)
  else:
    resultArr.append(1)
  row, col = nextRow, nextCol

print(minResult)

resultArr.reverse()
for num in resultArr:
  print(num)
