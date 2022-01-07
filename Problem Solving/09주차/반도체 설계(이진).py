import sys
input = sys.stdin.readline

def sol(nums,N):
    dp = [1] * N
    for i in range(1,N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


N = int(input())
nums = list(map(int,input().split()))
print(sol(nums,N))

4 2 6 3 1 5  dp= [1,1,1,1,1,1]
  2          dp= [1,1,1,1,1,1]
	6        dp= [1,1,2,1,1,1]
	  3      dp= [1,1,2,2,1,1]
	    1    dp= [1,1,2,2,1,1]
	      5  dp= [1,1,2,2,1,2]
	         dp= [1,1,2,2,1,3]