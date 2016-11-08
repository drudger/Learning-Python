# If you code like this you are not a Python guy! ;)
squares = []
for n in range(10):
    squares.append(n ** 2)

print(list(squares))

# This is better, one line, nce and readable
squares = map(lambda n: n ** 2, range(10))
print(list(squares))
