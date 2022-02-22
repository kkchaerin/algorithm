# 주사위(눈 6개) 3개를 던져서 상금을 받는 게임
'''
규칙
1. 같은 눈 3개 -> 10,000+(같은 눈)*1,000원
2. 같은 눈 2개 -> 1,000원+(같은 눈)*100원
3. 같은 눈 1개 -> (가장 큰 눈)*100원
'''
# n명이 참가했을 때
# 가장 많은 상금 수여자의 상금을 출력

n = int(input())

res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort() #오름차순
    a, b, c = map(int, tmp)

    if a==b and b==c:
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+(a*100)
    elif b==c:
        money = 1000+(b*100)
    else:
        money = c*100

    if money>res:
        res = money
print(res)


# 후기
'''
괜히 머리써서 어려운 문제인줄..
강의보고 풀었음. 
'''
