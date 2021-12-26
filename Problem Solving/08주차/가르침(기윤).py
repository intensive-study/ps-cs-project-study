import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())
strings = [set(input().strip()) for _ in range(n)]
answer = 0
table = [False] * 26
for ch in ('a', 'c', 'i', 'n', 't'): table[ord(ch)-ord('a')] = True

def solve(s, cnt):
    global answer
    if cnt == k-5:
        w = 0
        for string in strings:
            ok = True
            for ch in string:
                if not table[ord(ch)-ord('a')]:
                    ok = False
                    break
            
            if ok: w += 1
        
        answer = max(w, answer)
        return
    
    for i in range(s, 26):
        if not table[i]:
            table[i] = True
            solve(i+1, cnt+1)
            table[i] = False
        
if __name__ == "__main__":
    if k < 5: print(0)
    elif k == 26: print(n)
    else:
        solve(0, 0)
        print(answer)