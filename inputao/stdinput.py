# coding: utf-8
import sys


# Guarda o input padrão antes de substituí-lo.
builtin_input = input if sys.version_info[0] >= 3 else raw_input
