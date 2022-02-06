#K번째 숫자
def getKthNumber(paramList, numList):
    N = paramList[0]
    s = paramList[1]
    e = paramList[2]
    k = paramList[3]

    # N == numList.length
    tmpList = numList[s-1: e]
    tmpList.sort()
    return tmpList[k-1]
    


T = int(input())

paramLists = []
numLists = []
for i in range(0, T):
    paramLists.append(list(map(int, input().split())))
    numLists.append(list(map(int, input().split())))


for i in range(0, T):
    print("#"+str(i+1), getKthNumber(paramLists[i], numLists[i]))
    
    
    
###### 정답 ######
T=int(intput())
for i in range(T):
    n, s, e, k = map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t, a[k-1]))

    
###### 리뷰 ######
#1. sort() 내장 함수 사용!
#2. 너무 복잡하게 생각함.
    




