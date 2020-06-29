def isr (n):
    def fib_isr():
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b

    f = []

    for i in itertools.takewhile(lambda x: x < n, fib_isr()):
        f.append(i)
    return f
