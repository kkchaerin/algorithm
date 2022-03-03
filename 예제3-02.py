# 문자와 숫자가 섞인 문자열이 주어지면
# 그 중 숫자만 추출해 순서대로 자연수로 만든다.
# +) 첫자리가 0일때는 무시.

str = input()

num = 0
i = 1
for char in str:
    if char.isdigit() and char != '0':
        num = num*i + int(char)
        i*=10
print(num)

cnt = 0
for i in range(1, num+1):
    if num%i == 0 :
       cnt += 1
print(cnt)
        
