def foo():
    global x
    x = 666
    return x + 999

"""
foo() must be called first to assign value to the global variable x.
"""

# print(x)   # This will result in NameError

foo()
print(x)
