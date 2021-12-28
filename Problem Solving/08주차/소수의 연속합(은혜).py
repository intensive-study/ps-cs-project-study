N = int(input())

prime = [True for _ in range(N+1)]
primeArr = []

for i in range(2, N+1):
    if prime[i]:        
        primeArr.append(i)
        for j in range(2*i, N+1, i): # i씩 증가(2의 배수, 3의 배수 순서대로 False로 제거)
            prime[j] = False
    
right = 0
sum = 0
rslt = 0

for left in range(len(primeArr)):
    while right < len(primeArr) and sum < N:
        sum += primeArr[right]
        right += 1
    if sum == N:
        rslt += 1
    sum -= primeArr[left]
    
print(rslt)
        