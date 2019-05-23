# coding: utf-8
from __future__ import unicode_literals
import sys

# Guarda o input padrão antes de substituí-lo.
if sys.version_info[0] >= 3:
    builtin_input = input  # PY3
else:
    builtin_input = raw_input  #PY2


# Tenta ativar o readline se existir.
try:
    import readline
except ImportError:
    pass


def noop(value):
    return value


def input(prompt, convert=noop):
    while True:
        value = builtin_input(prompt)
        value = value.strip()

        try:
            value = convert(value)
        except ValueError:
            print('Entrada incorreta de dados. Tente novamente.')
        else:
            break

    return value


# Cheirinho de chulé.
raw_input = input


class SNInvalid(ValueError):
    pass


def SN(text):
    if text in 'Ss':
        valor = True
    elif text in 'Nn':
        valor = False
    else:
        raise SNInvalid('Digite S ou N.')

    return valor
