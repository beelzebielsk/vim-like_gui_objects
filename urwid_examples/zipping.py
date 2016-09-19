#!/usr/bin/env python

# Practice using the 'zip' function and simple generators.

questions = ['a', 'b', 'c', 'd'];

def style():
    while True:
        yield 'questions';

# Works as expected. The style() function keeps yielding the the value
# 'questions', thus creating those tuples.
print( *zip(style(), questions) );

# This doesn't work. It will treat the string itself as the iterable, thus
# trying to iterate through the letters themselves.
print( *zip('questions', questions) );
