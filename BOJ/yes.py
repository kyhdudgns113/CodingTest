x, y = map(int, input().split())

triangle = []
num = 0
for i in range(x - 1):
  triangle.append([])
  for j in range(x - 1 - i):
    triangle[-1].append(num)
    num += 1
    
result = []

for i in range(x - 1):
  for j in range(min(x - i - 1, y - i - 1)):
    result.append(triangle[i][j])

print(result)