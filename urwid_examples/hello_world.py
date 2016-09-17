#!/usr/bin/env python
import urwid;

txt = urwid.Text("Hello World");
fill = urwid.Filler(txt, 'middle');
loop = urwid.MainLoop(fill);
loop.run();
