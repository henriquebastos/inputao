# coding: utf-8
from __future__ import unicode_literals
from inputao.stdinput import builtin_input


def noop(value):
    return value

RETRY_MSG = 'Error. Try again.'

def input(prompt, convert=noop, msg=RETRY_MSG):
    while True:
        value = builtin_input(prompt)
        value = value.strip()

        try:
            value = convert(value)
        except ValueError as e:
            print(str(e) or msg)
        else:
            break

    return value


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
