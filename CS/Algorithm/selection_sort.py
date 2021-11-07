def selection_sort(l):
    n = len(l)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]


a = [2, 3, 4, 5, 1]  # unstable -> sort 후 2의 상대적 위치가 바뀜
print(a)
selection_sort(a)
print(a)
