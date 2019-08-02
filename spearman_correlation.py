import statistics


def pearson_cof(mx, my, stdx, stdy, X,  Y, n):
    return sum([(X[i] - mx)*(Y[i] - my) for i in range(n)])/(n * stdx*stdy)


def rank(data, fractional=False):
    R = [0 for i in data]
    _tup = [(n,i) for i,n in enumerate(data)]

    _tup.sort(key=lambda x: x[0])

    r = 1
    i = 0
    s = 1
    while i < len(_tup):
        j = i

        # counts the same numbers in the set
        while j < len(_tup) - 1 and _tup[j][0] == _tup[j + 1][0]:
            j += 1
        # equal number counter
        s = j - i + 1


        for j in range(s):
            # For each equal element use formula
            # obtain index of T[i+j][0] in A
            idx = _tup[i + j][1]
            if fractional:
                R[idx] = r + (s - 1) * 0.5
            else:
                R[idx] = float(r)

        if fractional:
            r += s
        else:
            r += 1
        i += s
    return R

if __name__ == "__main__":
    # X = [0.2, 1.3, .2, 1.1, 1.4, 1.5]
    # Y = [1.9, 2.2, 3.1, 1.2, 2.2, 2.2]

    n = input()
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))

    Rank_X = rank(X)
    Rank_Y = rank(Y)
    stdx = statistics.pstdev(Rank_X)
    stdy = statistics.pstdev(Rank_Y)
    m_X = statistics.mean(Rank_X)
    m_Y = statistics.mean(Rank_Y)

    print(f'{pearson_cof(m_X, m_Y, stdx, stdy, Rank_X, Rank_Y, len(X)):.3f}')



