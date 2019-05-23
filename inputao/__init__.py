# coding: utf-8


# Tenta ativar o readline se existir.
try:
    import readline
except ImportError:
    pass


from inputao.core import input, SN, SNInvalid


# No Python2, o nome é raw_input.
raw_input = input
