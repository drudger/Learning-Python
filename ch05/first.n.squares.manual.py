def get_squares_gen(n): 
    for x in range(n):
        yield x**2

squares = get_squares_gen(4) # this creates a generator object
print(squares) # <generator object get_squares_gen at ...>
print(next(squares)) # prints: 0
print(next(squares)) # prints: 1
print(next(squares)) # prints: 4
print(next(squares)) # prints: 9
# the followin raises StopIteration, the generator is exhausted,
# any further call to next will keep raising StopIteration
print(next(squares))
