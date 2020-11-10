
seq = [0, 1, 2, 3, 5]

print(seq[:])


a = ["a", "b", "c"]
b = [1, 2, 3, 4]

c = [a, b]

print(c)


"""
# Multiple Comment

List Method

.append(x)
.extend(iterable)
.insert(index, x)
.remove(index)
.pop([index])               # remove and return target(index).
.clear()
.index(x[, start[, end]])   # リスト中で x と等しい値を持つ最初の要素の位置をゼロから始まる添字で返します。
.count(x)
.sort(key=None, reverse=False)
.reverse()
.copy()
"""


# lambda list

seq = list(map(lambda x: x**2, range(10)))
# map(
#   (lambda method)
#   (array argument)
# )

# how of same writes
seq2 = [x**2 for x in range(10)]

print(seq)


# delete list item
del seq[0]  # side effects


# tuple unpack
tup = (123, 456, 789)
x, y, z = tup
print(x)
print(y)
print(z)



# 集合型(set) と 辞書型(dictionary)
## 集合型

# set は集合を扱かう方で、重複せず、順序がない
basket = {'apple', 'orange', 'apple'}
print(basket)
# > {apple, orange}

print('orange' in basket)
# > True

## 辞書型
tel = {'jack': 4098, 'spare': 41389}
del tel['jack']
print(tel)


# Loop technique
knights = {'gallahad': 'the pure', 'rubin': 'the brave'}
for kni, vit in knights.items():
  print(kni, vit)


for index, v in enumerate(['tic', 'tac', 'toe']):
  print(index, v)


