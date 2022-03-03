# N개의 수로 된 수열이 있다.
# 이 수열의 i번째부터 j번째 수까지의
# 합이 M이 되는 경우의 수를 구해라.

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0
for i in range(0, n):
    for j in range(0, n):
        sum = 0
        for k in range(i, j+1):
            sum += num_list[k]
        if sum == m:
            cnt += 1
print(cnt)
