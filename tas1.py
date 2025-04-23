from functools import singledispatch

@singledispatch
def pretty_print(var):
    print(f"{type(var)} - {var}")

@pretty_print.register(int)
def _(var):
    if var % 2 == 0:
        print(f"{var} is even number")
    else:
        print(f"{var} is odd number")

@pretty_print.register(float)
def _(var):
    print(f"Displaying with 2 decimal precision= {var:.2f}")

@pretty_print.register(str)
def _(var):
    print(f"Length= {len(var)}")
    print(f"Reverse Order= '{var[::-1]}'")

@pretty_print.register(dict)
def _(var):
    print(f"Number of keys= {len(var)}")
    print(f"Key-Value pairs= {var}")


pretty_print(8)
pretty_print(3.14159)
pretty_print("Hello World")
pretty_print("A very long string example to test the reversal and length handling.")
pretty_print({"x": 1, "y": 2})
pretty_print({"name": "Alice", "age": 30, "city": "Wonderland"})
pretty_print((3,6,7))