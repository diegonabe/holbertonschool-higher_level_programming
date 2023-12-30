#!/usr/bin/python3

if __name__ == "__main__":
    """Imprime el número y la lista de argumentos."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argumentos.")
    elif count == 1:
        print("1 argumento:")
    else:
        print("{} argumentos:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
