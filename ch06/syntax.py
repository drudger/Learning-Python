def func(arg1, arg2, and_so_on):
    pass
func = decoarg(argA, argB)(func)

# is equivalent to the following:

@decoarg(argA, argB)
def func(arg1, arg2, and_so_on):
    pass
