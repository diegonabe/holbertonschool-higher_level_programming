#!/usr/bin/python3
def uniq_add(my_list=[]):
    final = set(my_list)
    contador = 0
    for i in final:
        contador += i
    return (contador)
