# N개의 자연수가 입력되면
# 각 자연수의 자릿수의 합을 구하고
# 그 합이 최대인 자연수를 출력하기

n = int(input())
num_list = list(map(int, input().split()))

#자릿수 합 구하기
sum_list = []
for i in range(n):
    sum = 0
    num = num_list[i]
    for j in range(1, len(str(num_list[i]))+1):
        sum += (num%10)
        num = num//10
    sum_list.append(sum)

max=-2147000000
for i in range(n):
    if max < sum_list[i]:
        max = sum_list[i]

for i in range(n):
    if max == sum_list[i]:
        print(num_list[i])
        break
    

###### 리뷰 ######
# 정수 자릿수 합 구하는거 다 까먹었다..
