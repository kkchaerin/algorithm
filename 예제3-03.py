# 1~20 오름차순으로 놓인 카드의 리스트를
# 입력되는 범위만큼 역순으로 재정렬하라.

num_list = [i+1 for i in range(20)]

for i in range(10):
    a, b = map(int, input().split())

    tmp_list = num_list[a-1 : b]
    tmp_list.reverse()
    num_list[a-1 : b] = tmp_list

print(num_list)
