input()
N = set(input().split())
input()
M = list(input().split())

for m in M :
    if m in N:
        print(1)
    else:
        print(0)
        
# 리스트의 in 연산 시간 복잡도 O(N)
# Set과 Dictionary의 in 연산 시간 복잡도 O(1)
# 이분 탐색의 시간 복잡도 O(logN) 