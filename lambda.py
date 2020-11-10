# -*- coding: utf-8 -*-

# Higher order function
def make_incrementor(n):
  return lambda x: x+n

# Curry function
f = make_incrementor(42)

# Method call
print(f(1))
print(f(1))
print(f(5))

# Curry pattern
print(make_incrementor(42)(5))



pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key=lambda pair: pair[1])
print(pairs)

