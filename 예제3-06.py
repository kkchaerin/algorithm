# n개의 수로 이뤄진 수열이 있다.
# 이 수열의 i번째부터, j번째까지의 합이 M이 되는 경우의 수

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(n):
        sum = 0
        for k in range(i, j+1):
            sum += num_list[k]
        if m == sum :
            cnt += 1

print(cnt)
            
            


