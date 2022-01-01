import sys

input = sys.stdin.readline
n, r, c = map(int, input().split())
answer = 0

def solve(y, x, size):
    global answer
    if (y, x) == (r, c):
        print(answer)
        return

    if y <= r < y + size and x <= c < x + size:
        solve(y, x, size//2)
        solve(y, x+size//2, size//2)
        solve(y+size//2, x, size//2)
        solve(y+size//2, x+size//2, size//2)
    
    else: 
        answer += size**2

if __name__ == "__main__":
    solve(0, 0, 2**n)