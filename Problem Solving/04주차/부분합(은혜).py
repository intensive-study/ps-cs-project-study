import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
left, right = 0, 0
answer = 100000
sum = arr[right]

while True :
    
    if right == N:
        if left == 0:
            answer = 0
        break
    
    if sum >= S :
        answer = min(answer, right-left+1)
        if left < right:
            sum -= arr[left]
            left += 1
        else:
            right += 1
            if right < N : sum += arr[right]
    
    else :
        right += 1
        if right < N : sum += arr[right]

        
print(answer)
    


