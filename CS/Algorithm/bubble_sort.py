def bubble_sort(l):
    n = len(l)
    for i in range(n):
        flag = False
        for j in range(n - 1 - i):  # 한번 loop 돌때마다 뒤에서 i 번째까진 정렬되 있으므로 optimize 하기위해 -i 크기만큼 순회
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                flag = True
        if not flag:  # 한번 순회했는대도 flag 가 False 이면 이미 앞부분 정렬되어있기때문에 break 해서 optimize
            break


l = [8, 2, 3, 4, 5, 7]
print(l)
bubble_sort(l)
print(l)
