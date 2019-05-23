def noop(value):
    return value


builtin_input = input


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
