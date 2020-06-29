import itertools

def fib (n):
    def fib_vsr(n):
        a, b = 1, 1
        f = [a]
        while b < n:
            f.append(b)
            a, b = b, a + b
        return f

    f = []

    for i in itertools.takewhile(lambda x: x < n, fib_vsr(n)):
        f.append(i)
    return f
