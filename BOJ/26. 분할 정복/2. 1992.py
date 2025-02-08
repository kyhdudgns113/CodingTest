#
# n : 정사각형 배열 한 변의 길이
# board[][] : 정사각형 배열
#
# 상황 : 
#   배열을 정사각형 배열로 4등분 한다.
#   배열들이 전부 0이면 0, 전부 1이면 1
#   하나라도 다르면
#     (왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래)
#     이렇게 문자열을 만든다
#       예시 : (0110), (0(0101)1(1101))
#   이 과정을 반복한다.
# 
# 구하는것 : 최종적으로 만들어지는 문자열
# 풀이 : 상황에서 설명이 되었다.

import sys

input = sys.stdin.readline

n = int(input())

board = list(list(input().strip()) for i in range(n))

def recurse(r0, c0, len):
  if len == 1:
    return board[r0][c0]
  
  halflen = len // 2
  
  upLeft = recurse(r0, c0, halflen)
  upRight = recurse(r0, c0 + halflen, halflen)
  downLeft = recurse(r0 + halflen, c0, halflen)
  downRight = recurse(r0 + halflen, c0 + halflen, halflen)
  
  sumString = upLeft + upRight + downLeft + downRight
  if sumString == "0000":
    return "0"
  elif sumString == "1111":
    return "1"
  else:
    return "(" + sumString + ")"
  
print(recurse(0, 0, n))