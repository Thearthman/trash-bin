import math, re


def tokenize(_lexeme: str):
    _lexical_table = {'+': '001',
                      '-': '002',
                      '*': '003',
                      '/': '004',
                      '^': '005',
                      'sin': '006',
                      'cos': '007',
                      'e^': '008',
                      'log': '009',
                      '(': '010',
                      ')': '011',
                      }
    if _lexeme in _lexical_table:
        return _lexical_table[_lexeme]
    else:
        return _lexeme


def get_precedence(_lexeme: str):
    _precedence_table = {'+': 1,
                         '-': 1,
                         '*': 2,
                         '/': 2,
                         '^': 3
                         }
    return _precedence_table[_lexeme]


def is_operator(_lexeme: str):
    _lexical_table = {'+': '001',
                      '-': '002',
                      '*': '003',
                      '/': '004',
                      '^': '005',
                      'sin': '006',
                      'cos': '007',
                      'e^': '008',
                      'log': '009',
                      '(': '010',
                      ')': '011',
                      }
    return _lexeme in _lexical_table


def reverse_polish_notation(_lexical_list: list):
    _stage = 0
    _stack = [], [], [], [], [], [], [], []
    _output = []
    _last_precedence = 0
    for _lexeme in _lexical_list:
        if is_operator(_lexeme) and not (_lexeme == '(' or _lexeme == ')'):
            _current_precedence = get_precedence(_lexeme)
            if _current_precedence > _last_precedence:
                _stack[_stage].append(_lexeme)
            else:
                _output.append(_stack[_stage].pop())
                _stack[_stage].append(_lexeme)
            _last_precedence = get_precedence(_stack[_stage][len(_stack[_stage]) - 1])
        elif _lexeme == '(':
            _stage += 1
            _last_precedence = 0
        elif _lexeme == ')':
            _output.extend(reverse_polish_notation(_stack[_stage]))
            _stage -= 1
        else:
            _output.append(_lexeme)
    if len(_stack[_stage]) > 0:
        for _i in range(len(_stack[_stage])):
            _output.append(_stack[_stage].pop())
    return _output


def lexical_analysis(expression: str):
    _token_list = []
    _lexical_list = expression.split(' ')
    _lexical_list_RPN = reverse_polish_notation(_lexical_list)
    print(_lexical_list_RPN)
    # _token_list = expression.maketrans(lexical_table)
    for _lexeme in _lexical_list_RPN:
        _token_list.append(tokenize(_lexeme))
    print(_token_list)

# def differentiate_expression():

# def differentiateSingleTerm(expression: str, x="x", y="y"):
# extract functions like sin, exp and log

# def taylorExpansion(expression: str, x="x", y="y"):
# Lexical Analysis, extract single terms


lexical_analysis("2 / ( ( x + 3 ) * 4 + 4 )")

# y=sin(x)
# y=sin(x)*b
