#
# n : 정사각형 배열 한 변의 길이(n = 3^정수)
# board[][] : 정사각형 배열
#
# 상황
#   배열에는 각각 (-1, 0, 1) 중 하나가 채워져 있다.
#   배열이 전부 같은 숫자라면 해당 숫자에 해당하는 종이로 채운다.
#   그게 아니라면 같은 크기인 9개의 정사각형 배열로 쪼갠다.
#   각각 쪼갠 배열에 대하여 같은 연산을 수행한다.
#
# 구하는것
#   -1, 0, 1 종이를 각각 몇개 썼는지
#
# 풀이
#   배열을 9등분 한다.
#     각각 다음중 어느 경우인지 확인하고 ret 에 넣는다.
#       -1, 0, 1 : 각각의 숫자만으로 채워진다.
#       2 : 그 외의 경우
#     ret 마다 몇 번 나왔는지 확인한다.
#
#   만약 9번의 ret 가 전부 같으면서 2가 아니면 그 값을 리턴한다.
#   하나라도 다르면 각 ret 에 대해
#     result[ret] 를 1 더해준다.
#   
import sys

input = sys.stdin.readline

n = int(input())

board = list(list(map(int, input().split())) for i in range(n))

# result[-1] == result[3]
result = [0, 0, 0, 0]

# 리턴값
#   -1, 0, 1 : 이 숫자로만 채워져 있음
#   2 : 다른게 하나라도 있음
def recurse(r0, c0, n):
  if n == 1:
    return board[r0][c0]
  
  nextLen = n // 3
  
  partReturnValues = []
  
  # result 에 값을 한 번에 넣어주기 위해 만듦
  # 이걸 안 만들면 두 번 밑에있는 for 문이 9 * 9 로 돌아야됨.
  # 그게 그냥 마음에 안들어서 이렇게 구현했음.
  tempResult = [0, 0, 0, 0]
  
  for i in range(3):
    for j in range(3):
      ret = recurse(r0 + i * nextLen, c0 + j * nextLen, nextLen)
      tempResult[ret] += 1
      partReturnValues.append(ret)
  
  for i in range(9):
    if partReturnValues[i] != partReturnValues[0] or partReturnValues[i] == 2:
      for j in range(4):
        result[j] += tempResult[j]
      return 2
  
  return partReturnValues[0]

result[recurse(0, 0, n)] += 1

print(result[-1])
print(result[0])
print(result[1])

  