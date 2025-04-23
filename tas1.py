def pretty_print(var):
    if type(var) == int:
       if var % 2 == 0:
           print(f"{var} is even number")
       else:
           print(f"{var} is odd number")
    elif type(var) == float:
        print(f"Displaying with 2 decimal precision= {var:.2f}")
    elif type(var) == str:
        print(f"Length= " + str(len(var)) + "\nReverse Order= '" + var[::-1] + "'")
    elif type(var) == dict:
        print(f"Number of keys= {len(var)}" + "\nKey-Value pairs= " + str(var))
    else:
        print(str(type(var)) + " - " + str(var))

pretty_print(8)
pretty_print(3.14159)
pretty_print("Hello World")
pretty_print("A very long string example to test the reversal and length handling.")
pretty_print({"x": 1, "y": 2})
pretty_print({"name": "Alice", "age": 30, "city": "Wonderland"})
pretty_print((3,6,7))