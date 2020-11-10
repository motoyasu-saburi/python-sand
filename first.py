# fibonacci
a, b = 0, 1

while a < 10:
  print(a)
  a,b = b, a+b


#

intmax = 256 * 256
print(intmax)

intover = 256 * 256 + 1

print(intover)



# if
x = 20

if x < 0:
  print("x < 0")
elif x == 0:
  print("x == 0")
else:
  print("more")


# 拡張 for
words = ['cat', 'window', 'defenestrate']
for w in words:
  print(w, len(w))


# users = []
# for user, status in users.copy().items():
#   if status == 'inactive':
#     del users[user]


# range()

print(range(5))
for i in range(5):
  print (i)

for i in (range(0, 5)):
  print(i)


five_length = "aaaaa"
for i in (range(len(five_length))):
  if i == 4:
    continue
  elif i == 5:
    break

  print(i)


# pass

# > pass 文は何もしません。 pass は、文を書くことが構文上要求されているが、
# > プログラム上何の動作もする必要がない時に使われます:
# > pass のもう 1 つの使い道は、新しいコードを書いているときの関数や条件文の仮置きの本体としてです。
# > こうすることで、より抽象的なレベルで考え続けられます。 pass は何事も無く無視されます


