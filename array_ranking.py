def square_rank(data):
    R = []

    for i,n in enumerate(data):
        r = 1
        s = 0

        for j,nj in enumerate(data):
            if j != i and n > nj:
                r += 1
            elif j != i and nj == n:
                s+= 1
        if s > 1:
            R.append(float(r + 0.5 * (s - 1)))
        else:
            R.append(float(r))
    return R


def rankify_improved(A):
    # create rank vector
    R = [0 for i in range(len(A))]

    # Create an auxiliary array of tuples
    # Each tuple stores the data as well
    # as its index in A
    T = [(A[i], i) for i in range(len(A))]

    # T[][0] is the data and T[][1] is
    # the index of data in A

    # Sort T according to first element
    T.sort(key=lambda x: x[0])

    (rank, n, i) = (1, 1, 0)

    while i < len(A):
        j = i

        # Get no of elements with equal rank
        while j < len(A) - 1 and T[j][0] == T[j + 1][0]:
            j += 1
        n = j - i + 1

        for j in range(n):
            # For each equal element use formula
            # obtain index of T[i+j][0] in A
            idx = T[i + j][1]
            R[idx] = rank + (n - 1) * 0.5

        # Increment rank and i
        rank += n
        i += n

    return R

def rank(data, fractioned=False):
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
            if fractioned:
                R[idx] = r + (s - 1) * 0.5
            else:
                R[idx] = float(r)

        if fractioned:
            r += s
        else:
            r += 1
        i += s
    return R



if __name__ == "__main__":

    data = [20, 30, 10]
    # print(square_rank(data))
    X = [0.2, 1.3, .2, 1.1, 1.4, 1.5]
    Y = [1.9, 2.2, 3.1, 1.2, 2.2, 2.2]

    print(rank(X, False))
    print(rank(Y, False))