input()
N = list(input().split())
input()
M = list(input().split())

dic = {}

for n in N:
    dic[n] = dic.get(n, 0) + 1
        
for i in range(len(M)):
    M[i] = dic.get(M[i], 0)
    
print(*M)