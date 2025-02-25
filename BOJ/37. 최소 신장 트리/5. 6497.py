import sys
import heapq

input = sys.stdin.readline
output = sys.stdout.write

while True:
  M, N = map(int, input().split())
  
  if M == 0 and N == 0:
    break
  
  if M == 1 and N == 0:
    output("0\n")
    continue
  
  connections = [[] for _ in range(M)]
  isVisit = [False] * M
  initTotalLength = 0
  
  for _ in range(N):
    x, y, z = map(int, input().split())
    connections[x].append((z, y))
    connections[y].append((z, x))
    initTotalLength += z
    
  nextVisit = []
  heapq.heappush(nextVisit, (0, 0))
  
  finalLength = 0
  while nextVisit:
    dist, now = heapq.heappop(nextVisit)
    
    if isVisit[now]:
      continue
    
    for dist0, next in connections[now]:
      if not isVisit[next]:
        heapq.heappush(nextVisit, (dist0, next))
        
    finalLength += dist
    isVisit[now] = True
  
  output(f"{initTotalLength - finalLength}\n")