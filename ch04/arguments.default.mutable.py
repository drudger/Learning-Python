def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a)) # this will affect a's default vaule
    b[len(a)] = len(a) # and this will affect b's one

func()
func()
func()
