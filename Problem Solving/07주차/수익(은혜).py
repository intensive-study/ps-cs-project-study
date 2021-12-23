
import sys
input = sys.stdin.readline

while True:
    N = int(input())    
    if not N : break
    
    dp = []
    
    for i in range(N):
        P = int(input())
        pre = 0
        if i != 0:
            pre = dp[i-1]           
            
        dp.append(max(P, pre + P))  
       
    print(max(dp))