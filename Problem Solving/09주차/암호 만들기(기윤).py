import sys

input = sys.stdin.readline

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
x = ['a', 'e', 'i', 'o', 'u']

def solve(k, s, w):
    if k == l:
        cnt = 0
        for ch in w:
            if ch in x: cnt += 1
        
        if cnt >= 1 and l - cnt >= 2: print(''.join(w))
        
        return
    
    for i in range(s, c):
        w.append(alpha[i])
        solve(k+1, i+1, w)
        w.pop()

if __name__ == "__main__":
    w = []
    solve(0, 0, w)