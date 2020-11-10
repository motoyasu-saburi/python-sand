# -*- coding: utf-8 -*-

# file name import
import fibo

# method import
print(fibo.fib(1000))

# module name
print(fibo.__name__)


# method import
from fibo import fib, fib2
# from fibo import *
# from fibo import fib as fibonacci
print(fib(1000))
print(fib2(1000))