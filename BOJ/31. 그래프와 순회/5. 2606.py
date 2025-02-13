# n : 컴퓨터의 갯수
# m : 두 컴퓨터를 연결하는 경우의 수
# inps[] : (a, b) 연결하는 두 컴퓨터의 번호(1 <= a, b <= n)
#
# 상황
#   한 컴퓨터가 감염되면 연결된 모든 컴퓨터가 감염된다
#
# 구하는것
#   1번 컴퓨터가 감염되었을때
#   추가로 감염시키는 컴퓨터의 갯수
#
# 풀이
#   dfs 를 사용하였다.
#   bfs 를 사용해도 되었으나, 코드 짜는게 dfs 가 더 빠르다.

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
inps = list(list(map(int, input().split())) for i in range(m))

conn = [[] for i in range(n + 1)]
for inp in inps:
  a, b = inp
  conn[a].append(b)
  conn[b].append(a)

isVisit = [0 for i in range(n + 1)]

def dfs(now):
  isVisit[now] = 1
  
  for next in conn[now]:
    if isVisit[next] == 0:
      dfs(next)
dfs(1)     
print(sum(isVisit) - 1)