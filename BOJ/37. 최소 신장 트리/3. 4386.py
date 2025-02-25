from queue import PriorityQueue
import sys, math

input = sys.stdin.readline

N = int(input())

stars = [list(map(float, input().split())) for i in range(N)]
distArr = [
  [math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) for i in range(N)]
  for j in range(N)
]

nextVisit = PriorityQueue()
nextVisit.put([0, 0])

isVisit = [0 for i in range(N)]

result = 0

while nextVisit.qsize() > 0:
  dist, now = nextVisit.get()
  
  if isVisit[now] != 0:
    continue
  
  for next in range(N):
    if next != now and isVisit[next] == 0:
      nextVisit.put([distArr[now][next], next])
    
  isVisit[now] = 1
  result += dist
  
print(result)