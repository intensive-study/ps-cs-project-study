import sys

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

alpha = [False] * 26
d = ((0,1), (1,0), (-1,0), (0,-1))
answer = -1

def isin(y, x):
    if -1< y < r and -1 < x < c: return True
    return False

def dfs(y, x, cnt):
    global answer
    flag = True

    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if not isin(ny, nx): continue
        ch = ord(arr[ny][nx]) - ord('A')
        if alpha[ch]: continue

        alpha[ch] = True
        flag = False
        dfs(ny, nx, cnt+1)
        alpha[ch] = False
    
    if flag: answer = max(answer, cnt) 
        
if __name__ == "__main__":
    ch = ord(arr[0][0]) - ord('A')
    alpha[ch] = True
    dfs(0,0,1)
    print(answer)