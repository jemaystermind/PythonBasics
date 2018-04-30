from inspect import getsource


def add(x, y=10):
    return x + y


print("name: ", add.__code__.co_name)
print("module: ", add.__module__)
print("defaults: ", add.__defaults__)
print("bytecode: ", add.__code__.co_code)
print("local vars count: ", add.__code__.co_nlocals)
print("var names: ", add.__code__.co_varnames)

print("")

print(getsource(add))


# Assigning a function
def multiply_by_2(num):
    return num * 2

times_2 = multiply_by_2

print("2 * 2", times_2(2))


# Passing a function to a function
# Higher-order function in Kotlin

def do_math(func, num):
    return func(num)

print("Higher order function: 8 * 2 =", do_math(multiply_by_2, 8))


# Functions stored in a list

list_of_funcs = [times_2, add]

print("Functions inside a list: 5 * 2 =", list_of_funcs[0](5))
print("Functions inside a list: 5 + 10 =", list_of_funcs[1](5))
