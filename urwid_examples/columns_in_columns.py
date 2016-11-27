#!/usr/bin/env python
import urwid

leftColumns = ['00000', '00001']
rightColumns = [
    [
        [
            'a', 'b', 'c'
        ],
        [
            'd', 'e', 'f', 'g',
        ],
        [
            'h', 'i', 'j',
        ],
    ],
    [
        [
            'i', 'j', 'k'
        ],
        [
            'l', 'm',
        ],
        [
            'n', 'o', 'p',
        ],
    ],
]

left = list(map(lambda i: urwid.Text(i), leftColumns))
right = []
right.append( list(map(lambda i: urwid.Text('\n'.join(i)), rightColumns[0])) )
right.append( list(map(lambda i: urwid.Text('\n'.join(i)), rightColumns[1])) )

print(left)
print(right)

sessionColumns = list(map(lambda i: urwid.Columns(i), right))
sessionPile = urwid.Pile(sessionColumns)
idColumns = list(map(lambda i: urwid.Columns([i]), left))
columns = [urwid.Columns([x, y]) for (x,y) in zip(idColumns, [sessionPile]*2)]

urList = urwid.ListBox(columns)
fill = urwid.Filler(urList, height=('relative', 100) )
urwid.MainLoop(fill).run()

# Session Info: Text
# Session : Columnns of Session Info, as tall as tallest.
# Section : Pile of Sessions
# Section Pane: ListBox of Sections
