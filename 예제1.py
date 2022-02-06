#두 개의 자연수 N과 K가 주어졌을 때,
# N의 약수들 중 K번째로 작은 수를 구해라.

def getKthDivisor(n, k) :
    j = 0
    for i in range(1, n+1) :
        if n%i == 0 :
            j+=1
            if(j == k):
                return i

    return -1
            


n, k = map(int, input().split(' '))
res = getKthDivisor(n, k)
print(res)



############### 정답 ###############
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%1==0:
        cnt += 1
    if cnt==k
        print(i)
else:
    print(-1)
    
#### 리뷰
#파이썬에는 for-else 문법이 존재함.
