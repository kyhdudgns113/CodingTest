#
# N : 문제의 수
# M : 정보의 갯수
# input[] : (A, B) 로 이루어진 M 개의 배열. A 를 B 보다 먼저 풀어야됨
#
# 상황
#   쉬운문제(숫자가 낮은 문제)부터 풀려고 한다.
#   먼저 풀어야 할 문제가 있으면 먼저 푼다.
#
# 구하는것
#   문제를 푸는 순서
#
# 풀이
#   아래의 두 배열을 완성한다.
#     latersArr[A] : A 보다 늦게 풀어야 하는 문제들의 배열
#     numPrevArr[B] : B 보다 먼저 풀어야 하는 문제의 "갯수"
#   numPrevArr[A] == 0 인 A 들을 방문큐에 넣는다
#     방문큐는 "우선순위 큐" 이다.
#     선행해야 하는 문제가 없는 문제중에서 가장 숫자가 낮은것을 먼저 출력해야 한다.
#   방문큐의 맨 앞 원소를 now 라고 하자
#     now 를 출력한다.
#     now 가 선행문제인 문제들의 numPrev 를 1 줄인다.
#       만약 1 줄이고나서 0이 된다면 그 문제는 더이상 선행문제가 없는것이다.
#       방문큐에 넣는다.
#
# 연산량
#   input[] 을 통해 배열을 완성하는 연산 : O(M + N)
#   모든 숫자들을 우선순위 큐에 넣고 빼는 연산 : O(N log N)
#   = O(M + N log N)
#

from queue import PriorityQueue
import sys

input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().split())

latersArr = [[] for i in range(N + 1)]
numPrevArr = [0 for i in range(N + 1)]

for mm in range(M):
  A, B = map(int, input().split())
  latersArr[A].append(B)
  numPrevArr[B] += 1
  
nextVisit = PriorityQueue()
for i in range(1, N + 1):
  if numPrevArr[i] == 0:
    nextVisit.put(i)

while nextVisit.qsize() > 0:
  now = nextVisit.get()
  output("%d " % now)
  
  for next in latersArr[now]:
    numPrevArr[next] -= 1
    if numPrevArr[next] == 0:
      nextVisit.put(next)
