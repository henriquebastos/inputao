# coding: utf-8
import sys


# Guarda o input padrão antes de substituí-lo.
if sys.version_info[0] >= 3:
    builtin_input = input  # PY3
else:
    builtin_input = raw_input  #PY2
