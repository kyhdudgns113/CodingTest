#
# n : 점의 갯수
# m : 간선의 갯수
# connections[a] : (거리, 목적지) a 에서 목적지로 가는 간선의 길이. 이들의 배열이다
# start : 시작점
# end : 끝점
#
# 구하는것
#   시작점에서 끝점까지의 최단거리
#   이동할때 방문하는 점의 갯수
#   이동할때 방문하는 점의 경로 (start, end 포함)
#
# 풀이
#   다익스트라를 이용하여 풀 수 있다.
#   각 점마다 직전에 방문한 점을 기록한다.   
#

from queue import PriorityQueue
import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
m = int(input())

connections = [[] for i in range(n + 1)]
for mm in range(m):
  a, b, c = map(int, input().split())
  connections[a].append([c, b])
  
start, end = map(int, input().split())

prevInfo = [[10 ** 9, -1] for i in range(n + 1)]
  
nextVisit = PriorityQueue()
nextVisit.put([0, start, -1])

while nextVisit.qsize() > 0:
  dist, now, prev = nextVisit.get()
  
  if prevInfo[now][0] != 10 ** 9:
    continue
  
  for connection in connections[now]:
    dist0, next = connection
    nextVisit.put([dist + dist0, next, now])
    
  prevInfo[now] = [dist, prev]
  
print(prevInfo[end][0])

now = end

track = []

while now != -1:
  track.append(now)
  now = prevInfo[now][1]
  
track.reverse()
print(len(track))
for num in track:
  output("%d " % (num))