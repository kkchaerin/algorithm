
#n,m = 4, 6, 8, 12, 20 중 하나.
n, m = map(int, input().split())

cnt_list = [0]*(n+m+3) #list 초기화

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt_list[i+j] += 1

max=-2147000000
for i in range(n+m+1):
    if cnt_list[i] > max:
        max=cnt_list[i]
for i in range(n+m+1):
    if max == cnt_list[i]:
        print(i, end=' ')
