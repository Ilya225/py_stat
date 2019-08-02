import math

def gaus_distr(m, var, x):
    ex = math.e ** ((-(x - m)**2) / 2 * (var**2))

    return 1 / var* math.sqrt(2 * math.pi) * ex

# cumulative probability distribution (Cumulative distribution function)
def cdf(m, std, x):
    return 0.5 * (1 + math.erfc((x - m)/ (std * (2 ** 0.5))))


if __name__ == "__main__":
    cm = 250
    m = 2.4
    std = 2.0
    n = 100

    centr_m = n * m
    centr_std = (n ** (1/2)) * std

    p = cdf(centr_m, centr_std, 0) - cdf(centr_m, centr_std, cm)
    print(f'{p:.4f}')
