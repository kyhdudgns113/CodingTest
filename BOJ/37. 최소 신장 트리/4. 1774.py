#
# N : 점의 갯수
# M : 이미 연결된 간선의 갯수
# gods[] : 점들의 2차원 좌표값의 배열 (N 개)
# inp[] : 이미 연결된 간선의 배열 (M 개)
#
# 상황
#   모든 점들을 연결시키려 한다.
#
# 구하는것
#   추가로 연결해야할 길이중 최소값
#
# 풀이
#   최소 스패닝 트리 알고리즘을 응용하면 된다.
#   이미 연결된 간선에 포함된 두 점에 대하여
#     해당 점과 연결된 점들을 우선순위 큐에 넣는다.
#   이후 최소 스패닝 트리 알고리즘을 사용하면 된다.
#

from queue import PriorityQueue
import sys, math

input = sys.stdin.readline

N, M = map(int, input().split())
gods = [list(map(int, input().split())) for i in range(N)]

isVisit = [0 for i in range(N + 1)]
parentArr = [i for i in range(N + 1)]

nextVisit = PriorityQueue()

def distance(a, b):
  a -= 1
  b -= 1
  return math.sqrt((gods[a][0] - gods[b][0]) ** 2 + (gods[a][1] - gods[b][1]) ** 2)

def findRoot(a):
  if parentArr[a] == a:
    return a
  
  parentArr[a] = findRoot(parentArr[a])
  
  return parentArr[a]

def union(a, b):
  ra = findRoot(a)
  rb = findRoot(b)
  
  if ra == rb:
    return True
  
  if ra > rb:
    parentArr[ra] = rb
  else:
    parentArr[rb] = ra
    
  return True

for mm in range(M):
  A, B = map(int, input().split())

  if isVisit[A] == 0:
    for next in range(1, N + 1):
      if next != A and next != B and isVisit[next] == 0:
        nextVisit.put([distance(A, next), A, next])
    isVisit[A] = 1
  if isVisit[B] == 0:
    for next in range(1, N + 1):
      if next != A and next != B and isVisit[next] == 0:
        nextVisit.put([distance(B, next), B, next])
    isVisit[B] = 1
  
  union(A, B)

result = 0

while nextVisit.qsize() > 0:
  dist, prev, now = nextVisit.get()
  
  rPrev = findRoot(prev)
  rNow = findRoot(now)
  
  if rPrev == rNow:
    continue
  
  for next in range(1, N + 1):
    rNext = findRoot(next)
    if now != next and rNow != rNext:
      nextVisit.put([distance(now, next), now, next])
      
  union(prev, now)
  result += dist 

print("%.2f" % result)