#!/usr/bin/env python3
# Copyright (c) 2018 Podmogilniy Ivan
'''
Модуль дает несколько функций для форматирования строк
The Module provides a couple of functions to procedure strings.
>>> is_balanced('(Python (is (not (lisp))))')
True
>>> shorten("The Crossing road", 10)
'The Cro...'
>>> simplify(' some text with spurious whitespace ')
'some text with spurious whitespace'
'''

import string

def simplify(text, whitespace=string.whitespace, delete=''):
    '''
    Returns the string without spurious whitespace and delete rubbish symbols

    whitespace is the symbols named... delete is the rubbish symbols

    >>> simplify('hello world! ', delete = '!d')
    'hello worl'
    >>> simplify('hello ', delete = 'hello')
    ''
    >>> simplify(' this and that\t too')
    'this and that too'
    '''
    words = []
    word = ''
    for i in text:
        if i in delete:
            continue
        if i not in whitespace:
            word += i
        else:
            if word:
                words.append(word)
                word = ''
    if word:
        words.append(word)
        
    return ' '.join(words)
        
def is_balanced(text, brackets = '(){}[]<>'):
    '''
    Returns True if the  all brackets are balanced. Else return False

    >>> is_balanced('no brackets at all')
    True
    '''
    open_brackets = {}
    close_brackets = {}
    for Open, Close in zip(brackets[::2], brackets[1::2]):
        assert Open != Close, 'the bracket characters must differ'
        open_brackets[Open] = 0
        close_brackets[Close] = Open
    for char in text:
        if char in open_brackets:
            open_brackets[char] += 1
        elif char in close_brackets:
            open_bracket = close_brackets[char]
            if open_brackets[open_bracket] == 0:
                return False
            open_brackets[open_bracket] -= 1
    return not any(open_brackets.values())

def shorten(text, length = 25, indicator = '...'):
    '''
    Returns copy of text or shorted text with indicator
    (indicator in summary) if len(text) is more than length

    >>> shorten('My mom is crazy!', length = 1)
    Traceback (most recent call last):
    ...
    AssertionError: Sorry, "length" must be more or equal than "indicator" length
    >>> shorten('The best program in the world!', length = 1, indicator = '*')
    '*'
    '''
    assert length >= len(indicator), ('Sorry, "length" '
                            'must be more or equal than "indicator" length')
    return text[:length - len(indicator)] + indicator

if __name__ == '__main__':
    import doctest
    doctest.testmod()
