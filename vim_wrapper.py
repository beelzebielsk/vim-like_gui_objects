#!/usr/bin/env python

import urwid

class vim_wrapper(urwid.WidgetWrap):
    class modes():
        NORMAL = 'NORMAL'
        INSERT = 'INSERT'

    signals = ['mode_change']
    _selectable = True

    normal_bindings = {
        'j' : 'cursor down',
        'k' : 'cursor up',
        'h' : 'cursor left',
        'l' : 'cursor right',
        'i' : 'INSERT'
    }

    insert_bindings = {}

    def set_mode(self, mode):
        self.mode = mode
        self._emit('mode_change', self.mode)

    def show_args(*args):
        print(*args, sep='\n')

    def __init__(self, widget):
        self.mode = self.modes.NORMAL
        self.statusbar = urwid.Text(self.mode)
        urwid.WidgetWrap.__init__(self, urwid.Frame(widget, footer=self.statusbar) )

        alterBar = lambda bar, mode: self.statusbar.set_text(mode)
        urwid.connect_signal(self, 'mode_change', alterBar)

        self.normal_map = urwid.CommandMap().copy()
        self.normal_map._command = self.normal_bindings
        self._command_map = self.normal_map

    def keypress(self, size, key):

        if self.mode == self.modes.NORMAL:
            raise urwid.ExitMainLoop()
        else:
            self.set_mode(self.modes.NORMAL)


fill = urwid.Filler( urwid.Edit("ass") )
wrap = vim_wrapper(fill)
loop = urwid.MainLoop(wrap)
loop.run()
print(wrap._command_map._command)

# TODO
# - Connect the statusbar widget to the event which changes modes.
