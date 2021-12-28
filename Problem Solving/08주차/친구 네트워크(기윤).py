import sys

input = sys.stdin.readline

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)

    if pa == pb: return pa

    uf[pa] += uf[pb]
    uf[pb] = pa

    return pa


if __name__ == "__main__":
    tc = int(input())
    while tc:
        n = int(input())
        f2n = dict()
        uf = dict()
        cnt = 0

        for _ in range(n):
            a, b = input().split()
            if a not in f2n.keys():
                f2n[a] = cnt
                uf[cnt] = -1
                cnt += 1
            
            if b not in f2n.keys():
                f2n[b] = cnt
                uf[cnt] = -1
                cnt += 1
            
            k = merge(f2n[a], f2n[b])
            print(abs(uf[k]))
            
        tc -= 1