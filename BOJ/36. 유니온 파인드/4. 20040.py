# n : 점의 갯수
# m : 간선의 갯수
# inp[] : (a, b) 로 구성된 간선의 배열. 양방향임
#
# 상황
#   간선을 하나씩 배치한다.
#
# 구하는것
#   루프가 만들어지는 간선의 번호를 출력한다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]

def findRoot(a):
  if parents[a] == a:
    return a
  parents[a] = findRoot(parents[a])
  return parents[a]

def union(a, b):
  ra = findRoot(a)
  rb = findRoot(b)
  
  if ra == rb:
    return True
  
  if ra > rb:
    parents[ra] = rb
    return False
  else:
    parents[rb] = ra
    return False
result = 0
for mm in range(m):
  a, b = map(int, input().split())
  
  if union(a, b) == True and result == 0:
    result = mm + 1
  
print(result)

