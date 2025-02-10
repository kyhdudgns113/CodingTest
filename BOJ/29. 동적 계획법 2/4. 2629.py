# n : 추의 갯수
# a[] : 추의 무게들의 배열
# m : 구하고자 하는 무게의 갯수
# b[] : 구하고자 하는 무게의 배열
#
# 상황
#   양팔저울이 있다
#   양팔저울 양쪽에 주어진 추를 적절히 배치한다
#
# 구하는것
#   구하고자 하는 무게를 구할 수 있으면 "Y"
#   아니면 "N" 를 출력한다.
#
# 풀이
#   result[i][w] : i 번째 추까지 사용했을때 w 를 만들 수 있는지 여부
#   0 <= w <= 40000 에 대해
#     result[i][w] == "Y" 이면
#       result[i + 1][w] = "Y"이다.
#         i + 1 번째 추를 안 쓰면 된다.
#       result[i + 1][w + a[i]] = "Y"
#         구하려는 추 반대쪽에 i+1 번째 추를 추가하면 구할 수 있다.
#       result[i + 1][w - a[i]] = "Y"
#         구하려는 추 쪽에 i+1 번째 추를 추가하면 된다.
#
#       이 때 [w +- a[i]] 는 음수가 나올수도 있으며, 모두 계산한다.
#         추가 2, 3, 3 이라고 가정한다
#         다음과 같이 배치하면 무게가 4인 경우도 구할 수 있다.
#           왼쪽 : 2
#           오른쪽 : 3 3
#         이는 "-2 + 3 + 3" 으로 구해진다.
#         result[0][2] = "Y" 이며
#         result[0][-2] = "Y" 가 되도록 해야 한다.
#       배열의 범위를 0 부터 40000까지가 아니라
#       0 부터 80000 까지로 하고 40000보다 큰 인덱스는 음수를 의미하도록 하면 된다.

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = [["N" for i in range(80001)] for j in range(n)]

for i in range(n):
  result[i][0] = "Y"
  result[i][a[i]] = "Y"
  result[i][-a[i]] = "Y"
  if i > 0:
    for j in range(80001):
      if result[i - 1][j] == "Y":
        result[i][j] = "Y"
        result[i][(j + a[i]) % 80001] = "Y"
        result[i][(j - a[i])] = "Y"
        
print(*list(result[n - 1][bb] for bb in b))