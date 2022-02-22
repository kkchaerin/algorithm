# 점수계산

# 연속으로 정답인 경우,
# 두번째문제는 2점
# 세번째문제는 3점, ...
# k번째 문제는 k점
# 첫 정답=1점, 오답=0점

n = int(input())

ans_list = input().split() #문자열로 저장됨.
score = 0
j = 0
for i in ans_list:
    if i == '0':
        score += 0
        j = 0
    else:
        j += 1
        score += j

print(score)
