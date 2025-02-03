# res[n] : 길이 n 인 2진 수열의 갯수
#          =   길이 n-1 에서 "1" 을 추가한것
#            + 길이 n-2 에서 "00" 을 추가한것
# res[n] = res[n - 1] + res[n - 2]

n = int(input())

res = [0 for i in range(1000001)]
res[1] = 1
res[2] = 2

for i in range(3, n + 1):
  res[i] = (res[i - 1] + res[i - 2]) % 15746

print(res[n])