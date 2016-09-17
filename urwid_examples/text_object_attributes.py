#!/usr/bin/env python
import urwid;

def key_handler(key):
    if key in('q', 'Q'):
        raise urwid.ExitMainLoop();
    #txt.set_text(repr(key))
    txt.set_text(key)

txt = urwid.Text( ('banner', "Hello World"), align='center' );
fill = urwid.Filler(txt, 'top');
loop = urwid.MainLoop(fill, unhandled_input=key_handler);
loop.run();


