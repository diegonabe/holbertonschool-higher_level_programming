#!/usr/bin/python3
"""Lee desde la entrada estándar y calcula métricas.

Después de cada diez líneas o al interrumpir el teclado,
imprime las siguientes estadísticas:
    - Tamaño total del archivo hasta ese momento.
    - Conteo de códigos de estado leídos hasta ese momento.
"""


def print_stats(size, status_codes):
    """Imprime métricas acumuladas.

    Args:
        size (int): El tamaño acumulado del archivo leído.
        status_codes (dict): El recuento acumulado de códigos de estado.
    """
    print("Tamaño del archivo: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
