# inp[] : 전위순회로 들어오는 중복없는 이진 검색트리
#
# 구하는것
#   해당 이진트리를 후위순회로 한 줄씩 출력
#
# 풀이
#   주어진 범위의 전위순회 배열(VLR) 에 대하여
#     V 인 루트숫자는 맨 앞에 있다.
#     V 보다 큰 숫자는 R 이다.
#   이를 이용하여
#     V 보다 작은 범위에서 LRV 구하기
#     V 보다 큰 범위에서 LRV 구하기
#     V 출력
#   을 재귀함수로 구현했다.
#
# 연산량
#   트리의 노드 수를 n 이라 한다. (n <= 100,000)
#   모든 트리의 원소를 검색하는 연산을 log n 번 한다.
#     (start, end) 범위에서 LRV 를 구할때
#     (start, end) 범위에서 V 보다 큰 숫자의 인덱스를 찾는다.
#       이를 mid 라 한다.
#     이후 (start, mid), (mid + 1, end) 범위에서 각각 범위에서 찾는 연산을 한다.
#     연산을 할 때마다 범위가 절반씩 준다.
#     범위가 1이 될 떄 까지 연산을 하므로 log n 번 한다고 볼 수 있다.
#   = O(n log n) = 수백만
#

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
output = sys.stdout.write

vlr = []

while True:
  try:
    inp = input().strip()
    if len(inp) == 0:
      break
    vlr.append(int(inp))
  except:
    break
  
def getLRV(start, end):
  if start == end:
    output("%d\n" % vlr[start])
    return
  elif start > end:
    return
  
  lastLeft = start
  for i in range(start + 1, end + 1):
    if vlr[i] > vlr[start]:
      lastLeft = i - 1
      break
    
  getLRV(start + 1, lastLeft)
  getLRV(lastLeft + 1, end)
  output("%d\n" % vlr[start])

getLRV(0, len(vlr) - 1)
  