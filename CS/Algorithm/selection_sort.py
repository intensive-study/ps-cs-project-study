def selection_sort(l):  # unstable
    n = len(l)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]


l = [2, 3, 4, 5, 1]
# l = [2, 1, 2, 1] -> 같은 값의 상대적 위치 변함
print(l)
selection_sort(l)
print(l)
