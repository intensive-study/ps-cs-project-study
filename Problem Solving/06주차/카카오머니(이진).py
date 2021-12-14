# 424ms

import sys
input = sys.stdin.readline

n = int(input())
prev_balance = 0
charge_unit = 0 #최소 충전 단위
MAXI = 10 ** 18
min_balance = MAXI
available_value = True


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
    

for _ in range(n):
    money, balance = map(int, input().split())
    
    if prev_balance + money < 0:  # 충전이 필요한 경우
        if balance!= 0 and balance < min_balance:
            min_balance = balance
        charge_unit = gcd(balance - prev_balance - money, charge_unit)
        
        if charge_unit <= min_balance and min_balance != MAXI:
            available_value = False
            break
    else: #  prev_balance + a >= 0  # 충전 필요 없이 계산됨.
        if prev_balance + money != balance: # 잔액이 맞지 않는 경우
            available_value = False
            break
    prev_balance = balance 


if available_value and charge_unit != 0:
    print(charge_unit)
elif available_value and charge_unit == 0:
    print(1)
else:
    print(-1)         