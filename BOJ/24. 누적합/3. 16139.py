#
# S[] : 입력된 문자열을 list 로 바꾼것
#
# sums[c][k] : 0 부터 k 까지 (c + 1) 번쨰 알파벳이 존재하는 갯수
#
# idx : S[i] 가 몇 번째 알파벳인지 나타내는 수('a' = 0, 'b' = 1, ... 'z' = 25)
#
# l 번째부터 r 번째까지 S[i] 의 갯수
#   = sums[idx][r] - sums[idx][l - 1]

import sys

input = sys.stdin.readline
output = sys.stdout.write

S = list(input().strip())
q = int(input())
lens = len(S)

sums = [[0 for i in range(lens)] for j in range(26)]
sums[ord(S[0]) - ord('a')][0] = 1

for i in range(1, lens):
  c = S[i]
  idx = ord(c) - ord('a')
  for j in range(26):
    sums[j][i] = sums[j][i - 1]
  sums[idx][i] += 1

for _ in range(q):
  a, l, r = map(str, input().strip().split())
  l = int(l)
  r = int(r)
  idx = ord(a) - ord('a')
  output(str(sums[idx][r] - (sums[idx][l - 1] if l > 0 else 0)) + '\n')