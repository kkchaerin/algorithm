#k번째 큰 수

n, k = map(int, input().split())
numList = list(map(int, input().split()))


sumDict = {}
for i in range(0, n):
    for j in range(0, n):
        if (j!=i):
            for m in range(0, n):
                if(m!=j and m!=i):
                    sumDict[numList[i]+numList[j]+numList[m]] = 1
            
sumList = list(sumDict.keys())
sumList.sort(reverse=True)
print(sumList[k-1])

###### 정답 ######
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() #set 선언

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
            
res = list(res)
res.sort(reverse=True)
    



###### 리뷰 ######
#1. set 자료구조 : 중복을 허용하지 x
#2. set은 sort() 사용이 불가능함. 따라서, 리스트로 변환이 필요.
