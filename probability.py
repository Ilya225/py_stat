from math import factorial

# binomial distribution
# Enter your code here. Read input from STDIN. Print output to STDOUT

bi_dis = lambda n,r,p: (factorial(n) / (factorial(r) * factorial(n - r))) * ((p**r) * ((1-p)**(n-r)))

if __name__ == "__main__":
    b, n = list(map(float, input().split()))

    p = b/100

    n = int(n)
    bc = 0

    for r in range(2 + 1):
        bc += bi_dis(n,r,p)

    print(f'{bc:.3f}')

    bc = 0

    for r in range(2, n + 1):
        bc += bi_dis(n,r,p)
    print(f'{bc:.3f}')
