import sys

input = sys.stdin.readline
n, m = map(int, input().split())
coins = []
for _ in range(n):
    x = list(map(int, list(input().strip())))
    coins.append(x)

def find_one():
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if coins[i][j] == 1: return i, j
    
    return -1, -1

def reverse(y, x):
    for i in range(y+1):
        for j in range(x+1):
            if coins[i][j] == 0: coins[i][j] = 1
            else: coins[i][j] = 0

if __name__ == "__main__":
    answer = 0
    while True:
        y, x = find_one()
        if y == -1: break
        reverse(y, x)
        answer += 1
    
    print(answer)