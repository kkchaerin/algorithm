# n*n의 격자판이 주어지면
# 각 행의 합, 각 열의 합, 두 대각선의 합 중
# 가장 큰 합을 출력.

n = int(input())

num_map = [0]*n
for i in range(n):
    num_map[i] = list(map(int, input().split()))

max = 0

# 행의 합
for i in range(n):
    sum = 0
    for j in range(n):
       sum += num_map[i][j]
    if max < sum:
        max = sum

# 열의 합
for i in range(n):
    sum = 0
    for j in range(n):
        sum += num_map[j][i]
    if max < sum:
        max = sum

# 대각선 합 1
sum = 0
for i in range(n):
    sum += num_map[i][i]
if max < sum:
    max = sum

# 대각선 합 2
sum = 0
for i in range(n-1, 0, -1):
    sum += num_map[i][i]
if max < sum:
    max = sum

print(max)
        
    
