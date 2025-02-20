from collections import deque
import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

connections = [[] for i in range(n + 1)]

for nn in range(n - 1):
  a, b = map(int, input().split())
  connections[a].append(b)
  connections[b].append(a)
  
fathers = [-1 for i in range(n + 1)]
fathers[1] = 1

nextVisit = deque()
nextVisit.append(1)

while len(nextVisit) > 0:
  now = nextVisit.popleft()
  
  for next in connections[now]:
    if fathers[next] == -1:
      fathers[next] = now
      nextVisit.append(next)
      
for i in range(2, n + 1):
  output("%d\n" % fathers[i])