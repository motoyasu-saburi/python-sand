# -*- coding: utf-8 -*-

# default arguments


def ask_ok(prompt, retries=4, reminder="Please try agein!"):
  while True:
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise ValueError("invalid user response")
    print(reminder)


# pass over named argument
ask_ok("ok", retries=10)


# multiple arguments
def multipleArgument(*multipleArg):
  for arg in multipleArg:
    print(arg)



def documentaton_str():
  """
  先頭にドキュメンテーションを記載できる
  """
  return None


