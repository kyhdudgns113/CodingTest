# n : 점의 갯수
# m : 간선의 갯수
# r : 시작점의 번호
# inp[] : 시작점, 끝점 의 배열
#
# 상황
#   inp[i] 는 오름차순으로 정렬되어있다.
#   시작점 r 부터 dfs 를 수행한다.
#   방문한 순서대로 번호가 부여된다.
#
# 구하는것
#   각 점마다 방문한 순서를 출력한다.
#   방문한 적 없으면 0을 출력한다.

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
output = sys.stdout.write

n, m, r = map(int, input().split())
inp = list(list(map(int, input().split())) for i in range(m))

info = [[] for i in range(n + 1)]
for elem in inp:
  u, v = elem
  info[u].append(v)
  info[v].append(u)

for i in range(n + 1):
  info[i].sort()

isVisit = [0 for i in range(n + 1)]
visitNum = 1

def dfs(start):
  global visitNum
  isVisit[start] = visitNum
  visitNum += 1
  
  for end in info[start]:
    if isVisit[end] == 0:
      dfs(end)
      
dfs(r)

for num in range(1, n + 1):
  output(str(isVisit[num]) + '\n')

  