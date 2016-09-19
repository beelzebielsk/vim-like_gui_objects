#!/usr/bin/env python
import urwid;

# First step in using urwid.

txt = urwid.Text("Hello World");
fill = urwid.Filler(txt, 'middle');
loop = urwid.MainLoop(fill);
loop.run();
