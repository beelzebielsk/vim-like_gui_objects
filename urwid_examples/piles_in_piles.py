#!/usr/bin/env python
import urwid;

def key_handler(key):
    if key in('q', 'Q'):
        raise urwid.ExitMainLoop();
    elif key in ['t', 'T']:
        topPile.contents.append( ( urwid.Text( ('top', 't') ), mainPile.options() ) );
    elif key in ['b', 'B']:
        bottomPile.contents.append( ( urwid.Text( ('bottom', 'b') ), mainPile.options() ) );

pallete = [
        ('top', 'white', 'dark gray', 'bold'),
        ('bottom', 'dark gray', 'white', 'bold'),
]

mainPile = urwid.Pile([]);
container = urwid.Filler( mainPile, valign='top' );
divider = urwid.Divider('-');

topPile = urwid.Pile([]);
bottomPile = urwid.Pile([]);

mainPile.contents.append( ( topPile, mainPile.options() ) );
mainPile.contents.append( ( divider, mainPile.options()) );
mainPile.contents.append( ( bottomPile, mainPile.options() ) );

loop = urwid.MainLoop(container, pallete, unhandled_input=key_handler);
loop.run();
