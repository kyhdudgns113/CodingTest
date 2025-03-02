#
# N : 도시의 수 (N < 16)
# distances[i][j] : i 번째 도시에서 j 번째 도시로 갈 때 이동거리
#   연결되어있지 않다면 0
#
# 상황
#   시작도시 제외 모든 도시를 한 번씩만 방문한다.
#   시작도시에서 시작해서 시작도시로 끝낸다.
#
# 구하는것
#   최단거리
#
# 풀이
#   bitMask : i 번째 도시를 방문했으면 i 번째 비트가 1이다.
#   lengthArr[i][mask] : i 번째 도시에서 비트마스크가 mask 일때 최소값
#
#   점화식을 세우면
#     lengthArr[i][mask] = min(
#       lengthArr[next][mask + (2 ** next)] + distances[i][next]
#     )
#   이것을 조건을 잘 세우고 풀면 된다.
#
# 연산량
#   각 도시마다 모든 bitMask 값만큼 연산한다
#   = O(N) * O(2^N)
#   = O(N * 2^N)
#   = 1,048,576 (N = 16)
#

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input())

distances = [list(map(int, input().split())) for i in range(N)]
lengthArr = [[-1 for i in range(2 ** N)] for j in range(N)]

start = 1

def recurse(now, bitMask):
  global N, start
  
  if lengthArr[now][bitMask] != -1:
    return lengthArr[now][bitMask]
  
  result = 10 ** 9
  for next in range(N):
    if next != now and (bitMask & (2 ** next)) == 0 and distances[now][next] != 0:
      newMask = bitMask + (2 ** next)
      result = min(result, recurse(next, newMask) + distances[now][next])
  
  # now 가 마지막 도시인 경우 시작점과의 거리를 리턴해야 한다.
  # 첫 번째 조건 : 모든 도시를 방문했으면 비트에 숫자가 다 차있다.
  # 두 번째 조건 : 마지막 도시와 시작 도시 사이에 길이 존재한다.
  if bitMask == (2 ** N) - 1 and distances[now][start] != 0:
    result = distances[now][start]
    
  lengthArr[now][bitMask] = result
  return result

print(recurse(start, (2 ** start)))