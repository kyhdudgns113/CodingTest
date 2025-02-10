# pypy 로 돌려야 시간초과가 안뜬다.
# k : 파일의 갯수
# files[] : 파일의 크기 배열
#
# 상황
#   파일을 두 장씩 합친다.
#   두 장을 합칠때 각 장의 숫자를 더한다.
#   그 숫자만큼 비용을 지불한다.
#   모든 파일을 합칠때까지 반복한다.
#
# 구하는것
#   비용의 최솟값
#
# 풀이
#   f(start, end) : start 부터 end 까지 합쳤을때의 최소 비용
#     이는
#       앞 페이지 : (start, mid)
#       뒷 페이지 : (mid + 1, end)
#       각 페이지를 만들때의 최소비용 + 합칠때의 최소비용
#       = f(start, mid) + f(mid + 1, end) + sums(start, end) 이다.
#
#   위를 start <= mid < end 에 대하여 다음 반복문을 수행한다.
#
#   f(start, end) = min(
#     f(start, mid) + f(mid + 1, end) + sum(start, end)
#   )

import sys

input = sys.stdin.readline
output = sys.stdout.write

t = int(input())

k = 0
files = []
sums = [[]]
partResults = [[]]

def setSums():
  global k
  for start in range(k):
    for end in range(start, k):
      if start == end:
        sums[start][end] = files[start]
      else:
        sums[start][end] = sums[start][end - 1] + files[end]
        
def getResults(start, end):
  if start == end:
    partResults[start][end] = 0
    return 0
  if start + 1 == end:
    partResults[start][end] = sums[start][end]
    return partResults[start][end]
  
  # getResults(start, end) 가 중복으로 계산되는것을 방지한다.
  if partResults[start][end] != 10 ** 9:
    return partResults[start][end]
  
  for mid in range(start, end):
    partResults[start][end] = min(
      partResults[start][end],
      getResults(start, mid) + getResults(mid + 1, end) + sums[start][end]
    )
  
  return partResults[start][end]

for _ in range(t):
  k = int(input())
  files = list(map(int, input().split()))
  
  sums = [[0 for i in range(k)] for j in range(k)]
  setSums()
  
  partResults = [[10 ** 9 for i in range(k)] for j in range(k)]
  output(str(getResults(0, k - 1)) + '\n')
  
  