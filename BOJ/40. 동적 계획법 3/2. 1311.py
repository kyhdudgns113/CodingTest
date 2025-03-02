#
# pypy 로 돌려야 한다.
#
# N : 작업 및 사람의 수 (N <= 20)
# costArr[][] : 사람마다 작업을 처리할때 필요한 코스트트의 배열 (N * N)
#
# 상황
#   한 사람은 하나의 작업만 할 수 있다.
#   한 작업은 한 명의 사람만 할 수 있다.
#
# 구하는것
#   코스트 합의 최소값
#
# 풀이
#   bitMask : i 번째 사람이 배정된 작업이 있으면 i 번쨰 비트가 1이 된다.
#   resultArr[work][mask]
#     work 번째 작업이 할당되었을때 bitMask 가 mask 인 상태에서
#     코스트의 최소값
#
#   resultArr[work][mask] = min(
#     resultArr[work + 1][ i 번째 비트 빠진 mask] + costtArr[i][work]
#   )
#   이것을 재귀함수로 풀면 된다.
#
# 연산량
#   각 mask 마다 최대 작업의 개수만큼 연산한다
#     - 마스크의 갯수 : 2^N
#     - 작업의 갯수 : N
#     -> O(2^N) * O(N)
#     = O(N*2^N)
#     = 약 4천만
#   아슬아슬하게 1억이 안되어 가능하다.
#   pypy 로 돌려야 시간초과가 안난다.

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

N = int(input())

costArr = [list(map(int, input().split())) for i in range(N)]

resultArr = [[10 ** 9 for i in range(2 ** N)] for j in range(N)]

def recurse(workIdx, bitMask):
  global N

  if workIdx == N:
    return 0
  if resultArr[workIdx][bitMask] != 10 ** 9:
    return resultArr[workIdx][bitMask]
  
  result = 10 ** 9
  
  for peopleIdx in range(N):
    if ((2 ** peopleIdx) & bitMask) > 0:
      newMask = bitMask - (2 ** peopleIdx)
      result = min(result, recurse(workIdx + 1, newMask) + costArr[peopleIdx][workIdx])
      
  resultArr[workIdx][bitMask] = result
  return result

result = recurse(0, (2 ** N) - 1)

print(result)
    