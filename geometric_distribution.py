import math

def poisson_distr(k, lambd):
    return (math.e ** (-lambd) * (lambd ** k)) / math.factorial(k)

if __name__ == "__main__":
    lx = 0.88
    ly = 1.55

    CA = 160 + (lx + lx**2)
    CB = 128 + (ly + ly**2)

    print(CA)
    print(CB)