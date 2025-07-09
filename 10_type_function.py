print(type(3))
print(type(3.0))
print(type("3"))
# <class 'int'>
# <class 'float'>
# <class 'str'>

print("-----------")

print(type("True"))
print(type(True))
# <class 'str'>
# <class 'bool'>

print("-----------")

def hello():
    print("Hello world!")

print(type(hello))
print(type(print))
# <class 'function'>
# <class 'builtin_function_or_method'>