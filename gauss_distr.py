import math

def gaus_distr(m, var, x):
    ex = math.e ** ((-(x - m)**2) / 2 * (var**2))

    return 1 / var* math.sqrt(2 * math.pi) * ex

# cumulative probability distribution (Cumulative distribution function)
def cdf(m, std, x):
    return 0.5 * (1 + math.erfc((x - m)/ (std * (2 ** 0.5))))

# central limit theorem
def clt(n, m, std):
    m


if __name__ == "__main__":
    gg = 80
    gp = 60

    m = 70
    std = 10

    # f_res = cdf(m, std, gg) - cdf(m, std, gm)
    f_res = 1 - (cdf(m, std, 0) - cdf(m, std, gg))
    s_res = 1 - (cdf(m, std, 0) - cdf(m, std, gp))
    t_res = cdf(m, std, 0) - cdf(m, std, gp)

    print(f'{f_res * 100:.2f}')
    print(f'{s_res * 100:.2f}')
    print(f'{t_res * 100:.2f}')

# if __name__ == "__main__":
#     l1 = 19.5
#     l2 = 20
#     l3 = 22
#     m = 20
#     std = 2
#     f_res = cdf(m, std, 0) - cdf(m, std, l1)
#     s_res = cdf(m, std, l2) - cdf(m, std, l3)
#
#     print(f'{f_res:.3f}')
#     print(f'{s_res:.3f}')