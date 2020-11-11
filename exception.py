# -*- coding: utf-8 -*-

while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
    print("Oops!")
  except (RuntimeError, TypeError, NameError):
    pass



import sys

try:
  f = open('myfile.txt')
  s = f.readline()
  i = int(s.strip())

except OSError as err:
  print("OS Error: {0}".format(err))
except ValueError:
  print("Could not convert data to an integer.")
except:
  print("Unexpected error:", sys.exc_info()[0])
  raise
else:
  print("after process")
finally:
  print("finally")


