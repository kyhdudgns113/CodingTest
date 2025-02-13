# t : 테스트 케이스 개수
# l : 체스판 한 변의 길이
# r0, c0 : 나이트의 시작 지점
# ez, cz : 목표지점
#
# 구하는것
#   나이트가 목표지점으로 가는 가장 짧은 거리
#
# 풀이
#   bfs 로 풀면 된다.
#   queue 에 넣는 과정에서 isVisit 을 갱신해줬다.
#     이걸 여기서 안하면 nextQueue 에 중복된 값이 들어갈 수 있다.
#     최단거리를 구하는데는 문제가 없지만 시간이나 메모리가 부족해진다.

from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

t = int(input())

def bfs(l, isVisit, nextQueue: deque, row, col, nowCnt):
  isVisit[row][col] = nowCnt
  
  if row > 0 and col + 2 < l and isVisit[row - 1][col + 2] == 0:
    isVisit[row - 1][col + 2] = nowCnt + 1
    nextQueue.append({'row': row - 1, 'col': col + 2, 'cnt': nowCnt + 1})
  if row > 1 and col + 1 < l and isVisit[row - 2][col + 1] == 0:
    isVisit[row - 2][col + 1] = nowCnt + 1
    nextQueue.append({'row': row - 2, 'col': col + 1, 'cnt': nowCnt + 1})
  if row > 1 and col > 0 and isVisit[row - 2][col - 1] == 0:
    isVisit[row - 2][col - 1] = nowCnt + 1
    nextQueue.append({'row': row - 2, 'col': col - 1, 'cnt': nowCnt + 1})
  if row > 0 and col > 1 and isVisit[row - 1][col - 2] == 0:
    isVisit[row - 1][col - 2] = nowCnt + 1
    nextQueue.append({'row': row - 1, 'col': col - 2, 'cnt': nowCnt + 1})
  
  if row < l - 1 and col + 2 < l and isVisit[row + 1][col + 2] == 0:
    isVisit[row + 1][col + 2] = nowCnt + 1
    nextQueue.append({'row': row + 1, 'col': col + 2, 'cnt': nowCnt + 1})
  if row < l - 2 and col + 1 < l and isVisit[row + 2][col + 1] == 0:
    isVisit[row + 2][col + 1] = nowCnt + 1
    nextQueue.append({'row': row + 2, 'col': col + 1, 'cnt': nowCnt + 1})
  if row < l - 2 and col > 0 and isVisit[row + 2][col - 1] == 0:
    isVisit[row + 2][col - 1] = nowCnt + 1
    nextQueue.append({'row': row + 2, 'col': col - 1, 'cnt': nowCnt + 1})
  if row < l - 1 and col > 1 and isVisit[row + 1][col - 2] == 0:
    isVisit[row + 1][col - 2] = nowCnt + 1
    nextQueue.append({'row': row + 1, 'col': col - 2, 'cnt': nowCnt + 1})
  
    
  while len(nextQueue) > 0:
    elem = nextQueue.popleft()
    row0 = elem['row']
    col0 = elem['col']
    cnt = elem['cnt']
    return bfs(l, isVisit, nextQueue, row0, col0, cnt)
  
  return 0


for tt in range(t):
  l = int(input())
  r0, c0 = map(int, input().split())
  rz, cz = map(int, input().split())
  
  isVisit = [[0 for i in range(l)] for j in range(l)]
  nextQueue = deque()
  
  bfs(l, isVisit, nextQueue, r0, c0, 1)
  
  print(isVisit[rz][cz] - 1)