# 레거시 코드
# 원래 문제는 1 -> n -> v3 -> v2 -> n 같이 중간에 n 이 들어가도 허용을 한다.
# 이 코드는 허용을 안하도록 짠 코드다

from queue import PriorityQueue
import sys

input = sys.stdin.readline

n, e = map(int, input().split())
connections = [[] for i in range(n + 1)]

for ee in range(e):
  a, b, c = map(int, input().split())
  connections[a].append([b, c])
  connections[b].append([a, c])

v2, v3 = map(int, input().split())

def getLenWithout(start, end, no1, no2):
  global n
  distances = [10 ** 9 for i in range(n + 1)]
  distances[start] = 0
  
  nextVisit = PriorityQueue()
  for connection in connections[start]:
    end0, dist = connection
    if end0 != no1 and end0 != no2:
      nextVisit.put([dist, end0])
      
  while nextVisit.qsize() > 0:
    distance, now = nextVisit.get()
    
    if distances[now] != 10 ** 9:
      continue
    
    for connection in connections[now]:
      end0, dist = connection
      if end0 != no1 and end0 != no2 and distances[end0] == 10 ** 9:
        nextVisit.put([distance + dist, end0])
    
    distances[now] = distance
    
  return distances[end]

# 1 -> a -> b -> n 로 가는 최단경로를 구한다.
def getLen(a, b, n):
  
  # 1 -> a 경로를 구하되 b, n 은 지나지 않도록 한다.
  distance_1_to_a = 0
  if a == n:
    distance_1_to_a = getLenWithout(1, a, -1, -1)
  else:
    distance_1_to_a = getLenWithout(1, a, -1, -1)
    
    
  
  # a -> b 경로를 구하되 n 은 지나지 않는다. (1은 지나도 된다)
  # 지나면 안되는곳에 뭐라도 넣어야하니 -1을 넣는다.
  distance_a_to_b = 0
  if b == n:
    distance_a_to_b = getLenWithout(a, b, -1, -1)
  else:
    distance_a_to_b = getLenWithout(a, b, -1, -1)
    
  # b -> n 경로를 구한다.
  distance_b_to_n = getLenWithout(b, n, -1, -1)
  
  result = distance_1_to_a + distance_a_to_b + distance_b_to_n
  return result

distance_123n = getLen(v2, v3, n)
distance_132n = getLen(v3, v2, n)

if 10 ** 9 <= distance_123n or 10 ** 9 <= distance_132n:
  print(-1)
elif 10 ** 9 <= distance_123n:
  print(distance_132n)
elif 10 ** 9 <= distance_132n:
  print(distance_123n)
else:
  print(min(distance_123n, distance_132n))
