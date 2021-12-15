def make_heap(a):
    n = len(a)
    for i in range(n-1, -1, -1): heapify_down(a, i)

def delete_max(a):
    val = a[0]
    a[0] = a[-1]
    a.pop()
    heapify_down(a, 0)
    return val

def max_index(a, lp, rp, n, k):
    if lp >= n and rp >= n: return k
    if rp >= n:
        if a[lp] > a[k]: return lp
        return k
    
    if a[lp] > a[rp]:
        if a[lp] > a[k]: return lp
        return k
    
    if a[rp] > a[lp]:
        if a[rp] > a[k]: return rp
        return k
    
    if a[rp] == a[lp]:
        if a[lp] > a[k]: return lp
        return k

def heapify_down(a, k):
    n = len(a)
    while k < n:
        lp = 2 * k + 1
        rp = 2 * k + 2
        next_index = max_index(a, lp, rp, n, k)
        if next_index == k: break
        a[next_index], a[k] = a[k], a[next_index]
        k = next_index

length = int(input())
arr = []
for _ in range(length): arr.append(int(input()))
make_heap(arr)