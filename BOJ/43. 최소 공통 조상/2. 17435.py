#
# M : 수의 갯수 (M <= 200,000)
# F[i] : i + 1 이라는 수를 F 에 넣었을때 결과값
# Q : 쿼리의 수 (Q <= 200,000)
# queries[] : (N, X) 로 구성된 쿼리의 배열 (N <= 500,000, 1 <= X <= M)
#
# 상황
#   1 <= F[i] <= M 이다.
#   N, X 가 쿼리로 들어왔을때
#   F^N(X) 를 구하여라
#     F^1(X) = F(X)
#     F^2(X) = F(F(X))
#
# 풀이
#   1. F^1(X), F^2(X), F^4(X), F^8(X)... 를 구하고 저장한다.
#   2. 각 쿼리마다 N 을 2씩 나누면서 2로 나눴을때 나머지가 1이면 해당 F^a(X) 를 X 에 대입한다.
#     이 작업을 반복한다.
#
# 연산량
#   1 번 연산
#     모든 M 개의 숫자에 대해 log N 번 연산한다.
#     = O(M log N)
#   2 번 연산
#     각 쿼리 O(Q) 에 대해 O(logN) : O(Q log N)
#   = O(M log N + Q log N)
#
# 레거시 풀이
#   1. 브루트 포스
#     쿼리마다 일일히 계산한다.
#     쿼리 갯수마다 N 번 연산을 하게 된다.
#       = O(NP) = 천억
#     시간초과다.
#
#   2. 순환배열을 찾는다.
#     F(x) 는 결국 언젠가는 순환하는 부분이 생긴다.
#     1 -> 2 -> 3 -> 4 -> 5 -> 3 으로 입력이 주어질때
#     순환하지 않는 [1, 2, 3] 배열과 순환하는 [3, 4, 5] 배열을 만든다.
#     만약 N = 100, X = 1 이라면
#       1 은 순환하지 않는 배열중 [1, 2, 3] 배열의 0번째 원소이다.
#         N 은 이 배열의 끝까지 이동하는것(2) 보다 더 크다.
#         따라서 N 을 2를 뺀 98로 만든다.
#       3은 순환하는 배열 [3, 4, 5] 의 0번째 인덱스이다.
#       3에서 98번을 더 간다는건
#         98 % 3 = 2
#       즉 3에서 2만큼 이동하는것이랑 같으며 그 값은 5이다.
#     따라서 쿼리 (N, X) 가 (100, 1) 이면 그 값은 5 이다.
#
#     문제점
#       만약 [1, 2, 3] [3, 4, 5] 배열이 완성되었다고 가정하자.
#       그 뒤에 F[6] = 1 이 들어오면 순환하지 않는 배열 [1, 2, 3] 은
#         [6, 1, 2, 3] 이 되어야 한다.
#       만약에 남은 숫자 약 20만개에 대해서 특정 배열의 앞부분에만 계속 추가가 된다면
#         연산량은 O(M^2) = 400억 이 된다.
#       따라서 시간초과가 난다.
#       
import sys

input = sys.stdin.readline
output = sys.stdout.write

M = int(input())
F = list(map(int, input().split()))

Fnx = [[0 for i in range(M + 1)] for j in range(21)]

for i in range(M):
  Fnx[1][i + 1] = F[i]

for j in range(2, 21):
  for i in range(1, M + 1):
    Fnx[j][i] = Fnx[j - 1][Fnx[j - 1][i]]

Q = int(input())
for qq in range(Q):
  N, X = map(int, input().split())
  
  j = 1
  while N > 0:
    if N % 2 == 1:
      X = Fnx[j][X]
    j += 1
    N //= 2

  output("%d\n" % X)