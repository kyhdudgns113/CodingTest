#
# N : 학생의 수 (N <= 32,000)
# M : 키를 비교한 횟수 ( M <= 100,000)
# input[] : (A, B) 꼴의 크기 M 배열. 학생 A 가 학생 B 보다 크다는 뜻
#
# 상황
#   학생들을 키가 큰 순서대로 배열하려 한다.
#
# 구하는것
#   학생들을 배열하는 경우 중 하나를 출력한다.
#
# 풀이
#   1. input[] 값으로 아래 두 배열을 완성한다.
#     childsArr[i] : i 번째 학생보다 키가 작은 학생들의 배열
#     numParents[i] : i 번째 학생보다 키가 "큰" 학생중 남은 수
#   2. 자기보다 큰 사람이 없는 학생들을 큐에 넣는다.
#     numParents[i] 가 0 인 i 들을 모은다.
#   3. 큐에 학생이 있으면 반복문을 계속 돈다.
#     3.1. 학생 now 를 출력한다.
#     3.2. now 의 자식들은 그들보다 큰 사람중 now 가 사라진다.
#         - numParents 값을 1 낮춘다.
#     3.3. 만약 해당 자식의 numParents 값이 0이되면
#         - 더 이상 그 child 는 자기보다 큰 사람이 남아있지 않게 된다.
#         - 큐에 넣는다.
#
# 연산량
#   모든 간선들은 전부 확인한다 : O(M)
#   모든 학생들에 대해 연산한다 : O(N)
#   = O(M + N)
#   = 최대 10만
#

from collections import deque
import sys

input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().split())

childsArr = [[] for i in range(N + 1)]
numParents = [0 for i in range(N + 1)]

for mm in range(M):
  parent, child = map(int, input().split())
  childsArr[parent].append(child)
  numParents[child] += 1
  
nextVisit = deque()
for num in range(1, N + 1):
  if numParents[num] == 0:
    nextVisit.append(num)
    
while len(nextVisit) > 0:
  now = nextVisit.popleft()
  output("%d " % now)
  
  for child in childsArr[now]:
    numParents[child] -= 1
    if numParents[child] == 0:
      nextVisit.append(child)
      