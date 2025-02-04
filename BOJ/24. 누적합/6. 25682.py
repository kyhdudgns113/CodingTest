#
# n * m 크기의 체스판에서 k*k 크기로 잘라낸다.
# 잘라낸 판에서 색깔이 맞지 않는 부분은 다시 칠한다.
# 이 때 칠할 수 있는 가장 적은 횟수를 구한다.
#
#######   DEFINITION   ########
#
# board[][] : 입력받은 n * m 체스판
# sumRowIfB[row][col]
#   - (0, 0) 이 "B" 라고 할 때
#   - (row, col - k + 1) 부터 (row, col) 까지 칠해야 되는 갯수
# sumColIfB[row][col]
#   - (0, 0) 이 "B" 라고 할 때
#   - (row - k + 1, col) 부터 (row, col) 까지 칠해야 되는 갯수
#
# resultB[row][col]
#   - (0, 0) 이 "B" 라고 할 때
#   - (row - k + 1, col - k + 1) 부터 (row, col) 까지 칠해야 되는 갯수
#
#######   SOLUTION   #######
#
# resultB[row][col] 는 다음 2가지 방법중 하나로 구할 수 있다.
#   1. a + b - c
#     a : resultB[row - 1][col] : (row - 1, col) 까지 칠해야 하는 횟수
#     b : sumRowIfB[row][col] : (row, col) 의 행에서 칠해야 하는 횟수
#     c : sumRowIfB[row - k][col] : (row - k, col) 의 행에서 칠해야 하는 횟수
#   2. a + b - c
#     a : resultB[row][col - 1] : (row, col - 1) 까지 칠해야 하는 횟수
#     b : sumColIfB[row][col] : (row, col) 의 열열에서 칠해야 하는 횟수
#     c : sumColIfB[row][col - k] : (row, col - k) 의 열열에서 칠해야 하는 횟수
#
# sumRowIfB[row][col] 은 다음과 같은 점화식으로 구할 수 있다.
#   sumRow[row][col] = sumRow[row - 1][col] + a - b
#     a = 1 if (0, 0) 이 B 일때 (row, col) 이 바뀌어야 하는 경우
#     b = 1 if (0, 0) 이 B 일때 (row - k, col) 이 바뀌어야 하는 경우
# sumColIfB[row][col] 도 비슷하게 구할 수 있다.
# 인덱스 벗어나는 부분만 잘 처리하면 된다.
#
# 전체 작동 시간은
#     sumRow, sumCol 구하기 = O((n - k)*(m - k))
#   + resultB 구하기 = O((n - k) * (m - k))
#   = O(n * m) (왜냐하면 k < min(n, m))   
#
# n, m <= 2000 이므로 타당한 연산량이다.
# 
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = list(list(input().strip()) for i in range(n))

# (0, 0) 이 B 일때 해당 점을 포함한 K*K 에서 바꿔야 되는 갯수
resultB = [[0 for i in range(m)] for j in range(n)]

# (0, 0) 이 B 일때 해당 점을 포함한 열이나 해에서 바꿔야되는 갯수
sumRowIfB = [[0 for i in range(m)] for j in range(n)]
sumColIfB = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
  for j in range(k):
    c = "B" if (i + j) % 2 == 0 else "W"
    sumRowIfB[i][k - 1] += 1 if board[i][j] != c else 0
    
for i in range(m):
  for j in range(k):
    c = "B" if (i + j) % 2 == 0 else "W"
    sumColIfB[k - 1][i] += 1 if board[j][i] != c else 0
    
for row in range(n):
  for col in range(m):
    c = "B" if (row + col) % 2 == 0 else "W"
    c0 = "B" if (row + col - k) % 2 == 0 else "W"
    
    if row >= k:
      sumColIfB[row][col] = sumColIfB[row - 1][col]
      sumColIfB[row][col] += 1 if board[row][col] != c else 0
      sumColIfB[row][col] -= 1 if board[row - k][col] != c0 else 0
    if col >= k:
      sumRowIfB[row][col] = sumRowIfB[row][col - 1]
      sumRowIfB[row][col] += 1 if board[row][col] != c else 0
      sumRowIfB[row][col] -= 1 if board[row][col - k] != c0 else 0

for i in range(k):
  resultB[k - 1][k - 1] += sumRowIfB[i][k - 1]
  
for row in range(k - 1, n):
  for col in range(k - 1, m):
    if col > k - 1:
      resultB[row][col] = resultB[row][col - 1] + sumColIfB[row][col] - sumColIfB[row][col - k]
    elif row > k - 1:
      resultB[row][col] = resultB[row - 1][col] + sumRowIfB[row][col] - sumRowIfB[row - k][col]
      
result = n * m
for row in range(k - 1, n):
  for col in range(k - 1, m):
    result = min(
      result,
      resultB[row][col],
      k * k - resultB[row][col]
    )
    
print(result)
    
