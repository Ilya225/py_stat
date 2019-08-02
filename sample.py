import statistics


def quatitizer():
    n = input()
    nums = sorted(list(map(int, input().split())))
    if len(nums) % 2 != 0:
        fist_half = nums[:len(nums) // 2]
        second_half = nums[len(nums) // 2 + 1:]
    else:
        fist_half = nums[:len(nums) // 2]
        second_half = nums[len(nums) // 2:]
    print(fist_half)
    print(second_half)
    print(int(statistics.median(fist_half)))
    print(int(statistics.median(nums)))
    print(int(statistics.median(second_half)))


def median(mi, X_F_pairs, S):
    ss = 0
    for i, x_f_pair in enumerate(X_F_pairs):
        ss = ss + x_f_pair[1]
        if mi <= ss:
            # number of elements is even, search two numbers as median
            if S % 2 == 0:
                return float(x_f_pair[0]) if mi - ss < 0 else (x_f_pair[0] + X_F_pairs[i + 1][0]) / 2

            # number of elements is odd, median is in middle
            else:
                return float(x_f_pair[0])


def my_approach(X, F):
    S = sum(F)
    X_F_pairs = list(sorted(zip(X, F)))
    mi = S / 2
    # print(median(mi + mi/2, X_F_pairs, S) - median(mi - mi/2, X_F_pairs, S))


def naive(X, F, n):
    data = X
    freq = F

    s = []
    for i in range(n):
        s += [data[i]] * freq[i]
    N = sum(freq)
    s.sort()

    if n%2 != 0:
        q1 = statistics.median(s[:N//2])
        q3 = statistics.median(s[N//2+1:])
    else:
        q1 = statistics.median(s[:N//2])
        q3 = statistics.median(s[N//2:])

    ir = round(float(q3-q1), 1)
    # print(ir)

import math

if __name__ == "__main__":
    n = int(input())
    X = list(map(int, input().split()))
    mean = sum(X)/n
    sd = math.sqrt(sum(map(lambda x: (x - mean)**2, X))/n)
    print(f"{sd:.1f}")

