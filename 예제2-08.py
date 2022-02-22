# n개의 자연수가 입력되면
# 각 자연수를 뒤집은 후 (예) 910 -> 19)
# 그 수가 소수면 그 수를 출력.
# 단, 첫자리부터 연속된 0은 무시.

# 수 뒤집기
def reverse(x):
    return int(str(x)[::-1]) #뒤집
    

# 소수인지 체크
def isPrime(x):
    cnt = 0
    for i in range(1, x+1):
        if x%i == 0:
            cnt += 1
            
    if cnt == 2:
        return True
    else:
        return False

n = int(input())
num_list = list(map(int, input().split()))

for i in num_list:
    reversed_num = reverse(i)
    if isPrime(reversed_num):
        print(reversed_num, end=' ')
    
    
    
    
