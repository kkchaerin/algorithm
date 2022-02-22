#자연수 n이 입력되면
#1부터 n까지 소수의 개수를 출력
#제한시간 1초

n = int(input())

total_cnt = 0
for i in range(0, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt += 1

    if cnt == 2:
        total_cnt += 1

print(total_cnt)
