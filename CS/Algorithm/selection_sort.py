def selection_sort(l):  # unstable
    n = len(l)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]


a = [2, 3, 4, 5, 1]  # 단점 :
print(a)
selection_sort(a)
print(a)
