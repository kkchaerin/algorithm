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

