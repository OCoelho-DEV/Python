def gen1():
    print("COMEÇOU GEN 1")
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN 1')

def gen2(gen=None):
    print("COMEÇOU GEN 2")
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN 2')

g1 = gen2(gen1)

for n in g1:
    print(n)
