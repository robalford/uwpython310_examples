# Import this file in a Python interpreter to access variables and functions in the import_me namespace

# Or you can import specific names with from my_python_package.import_me import a_function

# See all the modules available in the current namespace with sys.modules

# Reload a module with importlib.reload(module)

var1 = "stuff"
var2 = "things"


def a_function():
    print("I'm a function")


print("All the code in the module gets run when it's imported")


if __name__ == "__main__":
    print("Except the code in this block")
