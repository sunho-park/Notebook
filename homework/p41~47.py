'''
def add(a, b): return a+b

add(1, 2)
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")

add(*[1, 2])

def doubler(f):
    return 2*f(x)

    return g

def f1(x):
    return x+1

g = doubler(f1)
assert g(3) == 8, "(3 + 1)*2 should equal 8"
assert g(-1) == 0, "(-1 + 1)*2 should equal 0"
'''
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")