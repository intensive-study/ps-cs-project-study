N = int(input())


def eratos(n):
    sieve = [1] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = 0

    return [i for i in range(2, n + 1) if sieve[i]]


def solution():
    primes = eratos(N)

    if not primes:
        return 0

    answer = 0
    head, tail = 0, 0
    acc = primes[0]

    while head <= tail:
        if acc < N:
            tail += 1
            if tail < len(primes):
                acc += primes[tail]
            else:
                break
        else:
            if acc == N:
                answer += 1
            acc -= primes[head]
            head += 1

    return answer


print(solution())