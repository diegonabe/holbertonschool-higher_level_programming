#!/usr/bin/python3

if __name__ == "__main__":
    """Imprime la suma de todos los argumentos"""
    import sys

    suma = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(suma))
