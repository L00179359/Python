cube_text = "Cube of X after import="

def cube(x):
    return x*x*x

print("Cube of X is=",cube(2))

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")