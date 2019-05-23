# Inputão

Um **input** melhor para ajudar os iniciantes em Python.

## Introdução

Quando o pessoal começa a programar em Python, muitos exercícios dependem da função _builtin_ `input`.

O problema é que o input do Python sempre retorna uma `string` e o iniciante acaba despendendo muita energia para validar os dados e pedir que o usuário digite novamente em caso de erro.

## Como usar

Instale com:

```
pip install inputao
```

Use no  seu código:

```python
from inputao import input
```

## Como funciona?

Importe o a função `input`.

```python
>>> from inputao import input
```

Por padrão input sempre retorna `string`.

```python
>>> nome = input('Qual o seu nome?')
>>> type(nome)
str
```

Para converter a entrada, informe a class como 2º parametro.

```python
>>> idade = input('Qual sua idade?', int)
>>> type(idade)
int
```

Ou, *por exemplo*, crie a uma função que valide o que voce quiser.

```python
>>> def SN(text):
>>>     if text in 'Ss':
>>>         valor = True
>>>     elif text in 'Nn':
>>>         valor = False
>>>     else:
>>>         raise ValueError('Digite S ou N.')
>>>     return valor

>>> continua = input('Deseja continuar? [Sn]', SN)
>>> type(continua)
bool
```

## Licença

MIT

## Autores

Rapaziada da Live.
