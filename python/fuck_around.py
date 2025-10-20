from scipy import stats

p_value = 1 - stats.binom.cdf(k=8, n=12, p=0.5) + stats.binom.cdf(k=3, n=12, p=0.5)

if __name__ == '__main__':
    print(p_value)