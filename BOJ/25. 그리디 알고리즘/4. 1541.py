#
# a + b - c + d - e + f - g ...
# 에서 임의로 괄호를 쳐가면서 구할 수 있는 값 중 최소값
# 이것을 구하는건 간단하다.
# 숫자를 계속 더하다가 - 가 나오면 그 뒤로는 다 빼기만 하면 된다.
# 한 번 - 가 나왔으면 그 뒤는 괄호를 적당히 쳐줌으로써 전부 빼줄 수 있다.

import sys

input = sys.stdin.readline

s = list(input().strip())
nums = []
ops = []

tempNum = 0
for c in s:
  if c != '-' and c != '+':
    tempNum *= 10
    tempNum += int(c)
  else:
    nums.append(tempNum)
    ops.append(c)
    tempNum = 0
nums.append(tempNum)
    
result = nums[0]
mulConstant = 1
for i in range(len(ops)):
  if ops[i] == '-':
    mulConstant = -1
  result += mulConstant * nums[i + 1]

print(result)