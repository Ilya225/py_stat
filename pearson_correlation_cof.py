import statistics

def pearson_cof(mx, my, stdx, stdy, X,  Y, n):
    return sum([(X[i] - mx)*(Y[i] - my) for i in range(n)])/(n * stdx*stdy)

if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))

    mx = statistics.mean(X)
    stdx = statistics.pstdev(X)
    my = statistics.mean(Y)
    stdy = statistics.pstdev(Y)

    print(f'{pearson_cof(mx,my,stdx,stdy,X,Y,n):.3f}')