# n : 수열의 길이
# a[] : 수열
# m : 찾는 숫자의 갯수
# b[] : 찾는 숫자들의 배열
#
# 구하는것 : 각 b 에 대하여 a 에 있으면 1, 없으면 0 출력
#
# 풀이
#   a 를 오름차순으로 정렬한다.
#   이분 탐색으로 원소들을 찾는다.
#
# 연산량
#   m 개에 대하여 log n 번 탐색을 수행한다.
#   = m log n

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

def find(val, l, r):
  if l == r:
    return 1 if a[l] == val else 0
  
  c = (l + r) // 2
  
  if val == a[c]:
    return 1
  elif val > a[c]:
    return find(val, c + 1, r)
  else:
    return find(val, l, c)
  
for bb in b:
  output(str(find(bb, 0, n - 1)) + '\n')

