#!/usr/bin/env python

import urwid

#texts = [urwid.Text(x) for x in ['a', 'b', 'c']*25]
texts = [urwid.Edit(x) for x in ['a', 'b', 'c']*25]

#fill = urwid.Filler( urwid.ListBox(texts), height=('relative', 100) )
fill = urwid.Filler( urwid.Pile(texts) )
urwid.MainLoop(fill).run()


