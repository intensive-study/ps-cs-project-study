import sys

input = sys.stdin.readline

def solve(n, arr):
    table = [1] * n

    for i in range(1, n):
        k = table[i]
        for j in range(i):
            if arr[j] <= arr[i]: continue
            k = max(k, table[j] + 1)
        
        table[i] = k
    
    return max(table)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))