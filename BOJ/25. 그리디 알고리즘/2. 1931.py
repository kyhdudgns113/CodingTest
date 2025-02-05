from functools import cmp_to_key
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
meetings = list(list(map(int, input().split())) for i in range(n))
    
def cmp(a, b):
  if a[1] < b[1]:
    return -1
  elif a[1] > b[1]:
    return 1
  elif a[0] > b[0]:
    return -1
  elif a[0] < b[1]: 
    return 1
  else:
    return 0
  
meetings.sort(key=cmp_to_key(cmp))

maxStartPoint = deque()
first = deque()
first.append(meetings[0])
maxStartPoint.append(first)

for i in range(1, n):
  if meetings[i][1] == meetings[i - 1][1]:
    maxStartPoint[-1].append(meetings[i])
  else:
    maxStartPoint.append(deque())
    maxStartPoint[-1].append(meetings[i])

minStart = 0
result = 0

while len(maxStartPoint) > 0:
  row = maxStartPoint.popleft()
  try:
    isSameHere = 0
    while len(row) > 0:
      meeting = row.popleft()
      if meeting[0] >= minStart:
        if meeting[0] < meeting[1]:
          minStart = meeting[1]
        else:
          isSameHere = meeting[1]
        result += 1
      else:
        break
    # (3, 3) 이나 (2, 2) 같은게 나왔을때
    minStart = isSameHere if isSameHere > 0 else minStart
  except:
    result = result + 0

print(result)
