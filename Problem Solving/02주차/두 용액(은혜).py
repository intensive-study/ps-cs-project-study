n = int(input())
sol = list(map(int, input().split()))
sol.sort()
l = 0
r = 1
answer = [[l,r]]
mix = 2e9

while True:
    
    if abs(sol[l]+sol[-r]) < mix and l+r < len(sol):
        mix = abs(sol[l]+sol[-r])
        answer.pop()
        answer.append([sol[l],sol[-r]])

    if sol[l] == sol[-r]:
        break
    if sol[l]+sol[-r] < 0:
        l += 1
    else:
        r += 1

print(" ".join(map(str, answer[0])))
