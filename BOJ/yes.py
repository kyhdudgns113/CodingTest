import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

def findLessCnt(val):
  global n
  result = 0
  for i in range(1, n + 1):
    if (val - 1) >= n * i:
      result += n
    elif val - 1 >= i:
      result += (val - 1) // i
    else:
      break
  return result    

arr = [findLessCnt(i) for i in range(1, n*n + 1)]

print(*arr)