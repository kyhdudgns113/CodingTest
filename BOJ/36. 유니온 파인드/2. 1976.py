# n : 도시의 갯수 (n <= 200)
# m : 여행할 도시의 갯수(m <= 1,000)
# connections[i][j] : i 번째 도시와 j 번째 도시가 연결되어있으면 1, 아니면 0
# cities[] : 여행할 도시의 순서
#
# 상황
#   순서대로 여행을 하려고 한다.
#
# 구하는것
#   연결이 되어있으면 YES, 아니면 NO 를 출력한다.
#
# 풀이
#   두 도시가 연결되어있는지 여부를 확인하면 된다
#   union 을 쓰면 된다.
#     두 집합 A, B 를 합칠때는
#       B 의 루트노드의 부모노드를 A 의 루트노드로 설정하면 된다.
#     두 도시 a, b 가 같은 집합인지를 확인할때는
#       재귀함수로 a 와 b 의 루트노드를 찾는다.
#       루트노드가 같은지 확인하면 된다.
#
# 연산량
#   1. 두 집합을 합칠때
#     모든 도시에 대하여, 합칠때마다 루트가 바뀌는 경우가 최악이다
#     = O(n) * O(n)
#     = O(n ^ 2)
#   2. 두 집합을 비교할 때
#     모든 여행할 도시에 대하여(m 개), 루트를 찾는데는 상수 시간이 걸린다.
#       - 이미 1번 연산에서 대부분은 자신의 부모가 루트와 매우 가깝다
#     = O(m) * O(1)
#     = O(m)
#   1 + 2 = O(n ^ 2 + m)

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
connections = [list(map(int, input().split())) for i in range(n)]
cities = list(map(int, input().split()))

parentArr = [i for i in range(n)]

def findRoot(a):
  if parentArr[a] == a:
    return a
  parentArr[a] = findRoot(parentArr[a])
  return parentArr[a]

def union(a, b):
  ra = findRoot(a)
  rb = findRoot(b)
  
  if ra > rb:
    parentArr[ra] = rb
  else:
    parentArr[rb] = ra

for i in range(n):
  for j in range(n):
    if connections[i][j] == 1:
      union(i, j)

result = "YES"
for i in range(m - 1):
  if findRoot(cities[i] - 1) != findRoot(cities[i + 1] - 1):
    result = "NO"
    break
  
print(result)
