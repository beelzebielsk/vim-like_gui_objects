#!/usr/bin/env python

import urwid
from urwid import ListBox, Text, Edit,\
        Filler, Columns, BoxAdapter,\
        GridFlow, AttrMap

# the solid fill is a placeholder.
# It will get replaced in the rest of the program.
fill = urwid.Filler(urwid.SolidFill(), height=('relative', 100) )
palette = [
    ('bright', '', 'yellow')
]
loop = urwid.MainLoop(fill, palette=palette)

def map_bright(widgets):
    return [AttrMap(x, None, focus_map='bright') for x in widgets]

############################################################
## An array of texts: {{{
############################################################

#texts = [urwid.Text(x) for x in ['a', 'b', 'c']*25]
#listbox = urwid.ListBox(texts)

############################################################
## }}}
############################################################

############################################################
## Another ListBox of Texts: {{{
############################################################

########## SETUP:
#texts = [Text(x) for x in ['a', 'b', 'c']*25]

########## BAD EXAMPLES:
# Not by itself, since the listbox needs to be told how high it is.
# (It's a box, and boxes get their dimensions from their containers)
#otherListBox = ListBox(texts)
#listbox = ListBox([otherListBox])

# This also doesn't work because `Filler` is used as a flow widget here.
#otherListBox = ListBox(texts)
#listbox = ListBox( [urwid.Filler(otherListBox,\
#        height=('relative', 100) )] )

# Still doesn't work because the containing widget is a box widget.
# There's no way to treat a ListBox like a flow widget.
#otherListBox = ListBox(texts)
#listbox = ListBox( [urwid.Filler(otherListBox, height='pack' )] )

########## GOOD EXAMPLES:
#otherListBox = ListBox(texts)
#filler = Filler(BoxAdapter(otherListBox, 10))
#listbox = ListBox( [BoxAdapter(filler, 10)] )

#otherListBox = ListBox(texts)
#filler = Filler(otherListBox, height=('relative', 100))
#listbox = ListBox( [BoxAdapter(filler, 10)] )

############################################################
## }}}
############################################################

############################################################
## Fillers: {{{ Requires a Box Adapter
############################################################

########## SETUP:
#texts = [Text(x) for x in ['a', 'b', 'c']*25]

########## BAD EXAMPLES:
#fillers = [Filler(x, height=('relative', 100)) for x in texts]
#listbox = ListBox(fillers)

#fillers = [Filler(x, height=10) for x in texts]
#listbox = ListBox(fillers)

#fillers = [Filler(x, height='pack') for x in texts]
#listbox = ListBox(fillers)

########## GOOD EXAMPLES:
#fillers = [ BoxAdapter(Filler(x, height='pack'), 1) for x in texts]
#listbox = ListBox(fillers)

#fillers = [ BoxAdapter(Filler(x), 1) for x in texts]
#listbox = ListBox(fillers)

############################################################
## }}}
############################################################

############################################################
## Columns : {{{
############################################################

########## SETUP:

# Can't be selected, so no switching.
#texts = [ Text(x) for x in ['a','b','c'] ]
# Using selectables allows for switching columns.
#texts = [ Edit(x) for x in ['a','b','c'] ]

#texts = map_bright(texts)

########## GOOD EXAMPLES:
#columns = Columns(texts)
#listbox = ListBox([columns]*10)

############################################################
## }}}
############################################################

############################################################
## GridFlow : {{{
############################################################

########## SETUP:
#texts = [ Edit(x*14) for x in ['a', 'b', 'c', 'd'] ]
#texts = map_bright(texts)

########## GOOD EXAMPLES:
#grid = GridFlow(texts, 10, 0, 0, 'center')
#listbox = ListBox([grid])

############################################################
## }}}
############################################################

if 'listbox' in dir():
    fill.original_widget = listbox
loop.run()
