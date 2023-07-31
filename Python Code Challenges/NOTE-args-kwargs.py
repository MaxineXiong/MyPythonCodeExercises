# Both functions can take in indefinite number of parameters
def foo_args(*args):
    return args  # returns a tupple of input arguments

def foo_kwargs(**kwargs):
    return kwargs  # returns a dictionary

print(foo_args(1, 2, 'hello', True))  # (1, 2, 'hello', True)
print(foo_kwargs(x = 1, y = 3, z = 9))  # {'x': 1, 'y': 3, 'z': 9}
