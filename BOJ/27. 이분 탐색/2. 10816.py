#
# n : 카드의 갯수
# cards[] : 카드에 적힌 수들의 수열
# m : 개수를 구하려는 횟수
# targets[] : 갯수를 구하고자하는 숫자들의 수열열
#
# 풀이
#   python 의 dic 자료구조에 cards 를 넣고
#   저장된 값들을 불러오기면 하면 된다.
#   읽기, 쓰기가 모두 log n 이다.
#   따라서 연산량은 m log n 이다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cnts = {}
for card in cards:
  try:
    cnts[card] += 1
  except:
    cnts[card] = 1

for target in targets:
  try:
    output(str(cnts[target]) + ' ')
  except:
    output("0 ")