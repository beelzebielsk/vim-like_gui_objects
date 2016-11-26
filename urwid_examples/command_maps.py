#!/usr/bin/env python

import urwid

def onpress(button):
    raise urwid.ExitMainLoop();

buttons = [
    'One',
    'Two',
    'Jake',
    'Four',
    'Why is he here?',
]

buttons = [urwid.Button(x,on_press=onpress) for x in buttons]

pile = urwid.ListBox( buttons )
fill = urwid.Filler( pile, height=('relative', 100) )
loop = urwid.MainLoop(fill)
#print( dir(buttons[0]) )
#print( dir(pile) )
#print( dir(loop) )

# Accessing the Command Map Itself. These two do the same thing.
#print( pile._command_map.__dict__['_command'] )
#print( pile._command_map._command )

############################################################
## Altering Command Map Globally: {{{
############################################################

## New key for existing command
#print( pile._command_map._command.update([ ('j', 'cursor down' ) ] ) )
#print( pile._command_map._command.update([ ('k', 'cursor up' ) ] ) )
#print( pile._command_map._command )

## The command map for everything is altered this way.
#print( buttons[0]._command_map._command )

############################################################
## }}}
############################################################

############################################################
## Altering the Command Map for just one element: {{{
############################################################

# New key for existing command
pile._command_map = pile._command_map.copy()
print( pile._command_map._command.update([ ('j', 'cursor down' ) ] ) )
print( pile._command_map._command.update([ ('k', 'cursor up' ) ] ) )
print( pile._command_map._command )

# The command map for everything is altered this way.
print( buttons[0]._command_map._command )

############################################################
## }}}
############################################################

############################################################
## New Command {{{
############################################################

# The command map doesn't call functions. It's just used to determine
# what a key is meant to do.
# So when defining a keypress function, you could make statements like
# if key == command_map['command']:
#   perform command
# Or, even better:
# if command_map[key] in [ ...list of possible commands... ]

#pile._command_map = pile._command_map.copy()
#pile._command_map._command.update( [('n', 'tisnew')] )
#print( pile._command_map._command )

############################################################
## }}}
############################################################

############################################################
## Which widgets get keypresses first? {{{
############################################################

# Answering the following questions:
# - Does pile container get press first, or contained button?
# - Whichever happens, does it happen consistently?
# To do this, will give two different actions for the same keypress to
# both widgets and see which action occurs.
pile._command_map = pile._command_map.copy()
buttons[0]._command_map = buttons[0]._command_map.copy()
print( buttons[0].keypress )

pile._command_map['j'] = 'cursor down'
buttons[0]._command_map['j'] = 'activate'

# 'activate' happens, rather than 'cursor down'.
# However, this doesn't mean that the button gets the signal first.
# It's still passed to it from up above, but the container classes
# pass it down to the focused element first before trying to process
# it themselves. Basically, if it gets processed, then `None` is
# returned, and if `None` is returned, then the key was handled. If
# not `None` is returned, then the key gets handled by the parent
# widget. Every widget can then do this up to the most high widget,
# which can then pass this key to the `unhandled_input` function.
# This is confirmed true for both ListBoxes and Piles.

############################################################
## }}}
############################################################

loop.run()
