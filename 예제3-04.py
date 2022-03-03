# 오름차순으로 정렬된 두 리스트를
# 오름차순으로 합쳐서 출력하라.

n = int(input())
n_list = map(int, input().split())

m = int(input())
m_list = map(int, input().split())

tmp_list = list()
tmp_list[:n] = n_list
tmp_list[n:n+m] = m_list
tmp_list.sort()

print(tmp_list)
