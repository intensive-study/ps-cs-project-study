def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        L, R = l[:mid], l[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    l = [3, 5, 1, 6, 7, 8, 4]
    print(l)
    merge_sort(l)
    print(l)
