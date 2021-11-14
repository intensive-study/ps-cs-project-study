import sys
from bisect import bisect_left

input = sys.stdin.readline


def LIS_with_dp():  # O(n^2)
    x = int(input())
    arr = list(map(int, input().split()))
    dp = [1 for i in range(x)]

    for i in range(x):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


def LIS_with_dp_and_bisect():  # O(nlog(n))
    N = int(input())
    input_list = list(map(int, input().split()))

    # dp input_list[0]로 초기화
    dp = [input_list[0]]

    for i in range(N):
        # 현재 순회중인 원소가 dp에 제일 마지막에 들어간 값보다 크면 dp에 값을 추가해주기
        if input_list[i] > dp[-1]:
            dp.append(input_list[i])
        # 현재 순회중인 원소가 dp의 마지막 값보다 작을시, 그 값을 dp에서 이분탐색하여 들어갈수 있는 위치에 넣기
        else:
            idx = bisect_left(dp, input_list[i])
            dp[idx] = input_list[i]

    print(len(dp))


if __name__ == '__main__':
    LIS_with_dp()
    LIS_with_dp_and_bisect()

'''
6
10 20 12 30 20 50
'''
