# N : 사람의 수 (N < 500)
# inputSequence[] : 1등부터 순서대로 사람을 나열한 배열
# M : 순위가 바뀐 경우의 수 (M <= 25,000)
# toggleArr[] : (A, B) 꼴의 크기 M 인 배열. A 와 B 가 순서가 바뀌었다는 뜻
#
# 상황
#   순서가 바뀐 모든 경우는 전부 입력으로 주어진다.
#
# 구하는것
#   1. 경우의 수가 2 이상인 경우
#     - ? 을 출력
#   2. 경우의 수가 0 인 경우
#     - IMPOSSIBLE 을 출력
#   3. 경우의 수가 1 인 경우
#     - 바뀐 순서를 출력
#
# 풀이
#   inputSequence 가 주어지면 본인보다 앞 순서에 있는 사람들을 전부 저장한다.
#     isFaster[][] 에 저장한다.
#     isFaster[A][B] : A 보다 B 가 더 앞순서에 있으면 1, 아니면 0
#     isFaster[A][0] : A 보다 앞 순서에 있는 사람의 수
#
#   다음 반복문을 돈다.
#     isFaster[i][0] == 0 인 숫자들을 방문큐에 넣는다.
#     i 를 다음 출력큐에 넣는다.
#       다음번 출력으로 정한다.
#     i 를 제거한다
#       isFaster[next][i] == 1 인 next 들을
#       isFaster[next][i] 를 0으로 만들고
#       isFaster[next][0] 을 1 줄인다.
#       
#       만약 isFaster[next][0] == 0 이면
#         next 보다 앞 순서에 있는 사람은 남아있지 않다는 뜻이다.
#         next 를 방문큐에 넣는다.
#
#   반복문을 도는 과정과 이후에 다음을 체크한다.
#     만약 방문큐의 크기가 2 이상이면 중복된 경우가 있다는 뜻이다.
#       - 자기보다 앞선 사람이 없는 경우가 2 이상 있다는 뜻이다.
#       - 그 중 누가 먼저 출력되도 괜찮다는 것이다.
#       - 즉, 중복된 경우가 있다는 의미다.
#     만약 방문큐의 크기가 0인데 남아있는 사람이 있다.
#       - 자기보다 앞선 사람이 없는 경우가 없다는 뜻이다.
#       - 남아있는 사람은 있는데, 출력할 사람은 없다.
#       - 이는 수열을 만드는것이 불가능하므로 IMPOSSIBLE 을 출력한다.
#
# 연산량
#   1번 연산(코드 주석에 있다.)
#     모든 사람에 대하여 : O(N)
#     자기보다 뒷 순서에 있는 사람들에 대한 연산을 한다 : O(N)
#     = O(N^2)
#   2번 연산
#     모든 toggleArr 원소에 대하여 우위관계를 바꾼다.
#     = O(M)
#   3번 연산
#     모든 사람중에서 자기보다 앞선 사람이 없는 경우를 찾는다.
#     = O(N)
#   4번 연산
#     모든 사람은 한 번씩 제거가 될 수 있다. : O(N)
#     각 사람에 대하여 나머지 모든 사람들에 대하여 확인한다 : O(N)
#     = O(N^2)
#   전부 더하면
#     O(N^2 + M) = 최대 25만 이 된다.
#   

from collections import deque
import sys

input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

for testCase in range(T):
  N = int(input())
  inputSequence = list(map(int, input().split()))
  
  M = int(input())
  toggleArr = [list(map(int, input().split())) for i in range(M)]
  
  # isFaster[A][B] : B 가 A 보다 앞에 있으면 1, 아니면 0
  # isFaster[A][0] : A 보다 앞에 있는 사람의 수
  isFaster = [[0 for i in range(N + 1)] for j in range(N + 1)] 
  
  # 1. 초기 우위관계를 설정한다.
  for nowIdx in range(N):
    now = inputSequence[nowIdx]
    
    for nextIdx in range(nowIdx + 1, N):
      next = inputSequence[nextIdx]
      isFaster[next][now] = 1
      isFaster[next][0] += 1
  
  # 2. 바뀐 우위관계를 설정한다.
  for a, b in toggleArr:
    if isFaster[a][b] == 0:
      isFaster[a][b] = 1
      isFaster[b][a] = 0
      
      isFaster[a][0] += 1
      isFaster[b][0] -= 1
    else:
      isFaster[a][b] = 0
      isFaster[b][a] = 1
      
      isFaster[a][0] -= 1
      isFaster[b][0] += 1
  
  # 3. 자기보다 순위 높은게 없는 친구들을 방문큐에 넣는다.
  nextVisit = deque()
  remain = N
  for people in range(1, N + 1):
    if isFaster[people][0] == 0:
      nextVisit.append(people)
      
  # 4. 방문큐에 있는 숫자를 now 라고 한다.
  #     now 를 출력큐에 넣는다.
  #     now 보다 뒷 순서에 있는 친구들은 더이상 자기 앞에 now 가 없어지게 된다.
  #       - 뒷 순서 친구들은 자기보다 앞에 있는 사람수를 1 줄인다.
  #     만약 뒷 순서 친구들중 자기보다 앞에 있는 사람이 없는 경우는 방문큐에 넣는다.
  #
  #   Case 1. 방문큐의 크기가 0 인 경우
  #     남아있는 사람이 없거나
  #     전부 자기보다 앞 순서인 사람이 하나 이상은 존재한다는 뜻이다.
  #     이런 경우는 존재할 수 없으므로 IMPOSSIBLE 을 출력한다.
  #
  #   Case 2. 방뮨큐의 크기가 2 이상인 경우
  #     방문큐에 있는 사람들 모두가 자기보다 앞 순서인 사람이 없다.
  #     이 사람중 누구를 먼저 출력해도 된다
  #     즉, 경우의수가 여럿 존재하게 된다.
  #     ? 를 출력해야 한다.
  #
  # newSequence : 출력할 배열
  newSequence = deque()
  while len(nextVisit) == 1:
    now = nextVisit.popleft()
    newSequence.append(now)
    remain -= 1
    
    for next in range(1, N + 1):
      if isFaster[next][now] == 1:
        isFaster[next][now] = 0
        isFaster[next][0] -= 1
        
        if isFaster[next][0] == 0:
          nextVisit.append(next)
          
  if len(nextVisit) > 1:
    output("?\n")
  elif remain > 0:
    output("IMPOSSIBLE\n")
  else:
    for num in newSequence:
      output("%d " % num)
    output("\n")
  
  
