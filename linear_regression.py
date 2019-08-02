import statistics


def pearson_cof(mx, my, stdx, stdy, X,  Y, n):
    return sum([(X[i] - mx)*(Y[i] - my) for i in range(n)])/(n * stdx*stdy)


def a_param(X, Y, n):
    return round(statistics.mean(Y) - b_param(X, Y, n) * statistics.mean(X), 3)


def b_param(X, Y, n):
    xy_sum = sum([x*y for x,y in zip(X,Y)])
    x_sum = sum(X)
    y_sum = sum(Y)
    x_sum_of_square = sum([x**2 for x in X])
    x_square_sum = x_sum**2

    return (n * xy_sum - x_sum * y_sum) / (n * x_sum_of_square - x_square_sum)


def b_param_pearson(X,Y, n):
    stdx = statistics.pstdev(X)
    stdy = statistics.pstdev(Y)
    mx = statistics.mean(X)
    my = statistics.mean(Y)
    return pearson_cof(mx, my, stdx, stdy, X, Y, n) * (stdy/stdx)


def linear_regression(a, b, x):
    return a + (b * x)

if __name__ == "__main__":

    X = [95, 85, 80, 70, 60]
    Y = [85, 95, 70, 65, 70]
    n = 5

    b = b_param_pearson(X,Y,n)
    a = a_param(X,Y,n)
    print(f'{linear_regression(a, b, 80):.3f}')