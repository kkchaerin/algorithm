#대표값
from collections import defaultdict

n = int(input())
score_list = list(map(int, input().split()))

#TODO 1. 평균 구하기
avg = round(sum(score_list)/n)

#TODO 2. 평균에 가까운 학생 구하기
avg_student = defaultdict(list) #append 사용하기 위함.
for i in range(0, n):
    gab = abs(avg - score_list[i])
    avg_student[gab].append(i)

avg_student = sorted(avg_student.items())

#평균의 가까운 학생이 여러명일 때.
length = len(avg_student[0][1])
if (length > 1):
    tmp = {}
    for i in range(0, length):
        tmp[avg_student[0][1][i]] = score_list[avg_student[0][1][i]]
    
#i) 점수 높은 사람
sorted_list = sorted(tmp.items(), reverse=True, key=lambda item: item[1])

tmp = defaultdict(list)
for i in sorted_list:
    tmp[i[1]].append(i[0])

sorted_list = sorted(tmp.items(), reverse=True)

number_list = []
#ii) 번호가 빠른 사람
if len(sorted_list[0][1]) > 1:
    number_list = sorted_list[0][1]
    number_list.sort()
    
print(avg, end=' ')        
print(number_list[0]+1)

        
    



