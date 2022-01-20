#Function to generate binary numbers from 1 to N using a queue.
def generate(N):
    s = [0]*N
    for i in range(1, N+1):
        n, k = i, 1
        while n:
            s[i-1] += (n&1)*k
            n >>= 1
            k *= 10
    return s