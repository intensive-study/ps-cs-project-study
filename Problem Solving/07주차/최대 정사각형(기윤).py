import sys

input = sys.stdin.readline

def solve(n, m, arr):
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    answer = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            table[i][j] = arr[i-1][j-1]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if table[i][j]: 
                table[i][j] = min(table[i-1][j], table[i][j-1], table[i-1][j-1]) + 1
                answer = max(answer, table[i][j])
    
    return answer

if __name__ == "__main__":
    while True:
        n, m = map(int, input().split())
        if (n, m) == (0, 0): break
        arr = [list(map(int, input().split())) for _ in range(n)]
        print(solve(n, m, arr))