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

    def set_mode(self, mode):
        self.mode = mode
        self._emit('mode_change', self.mode)

    def show_args(*args):
        print(*args, sep='\n')

    def __init__(self, widget):
        self.mode = self.modes.NORMAL
        self.statusbar = urwid.Text(self.mode)
        urwid.WidgetWrap.__init__(self, urwid.Frame(widget, footer=self.statusbar) )
        #urwid.connect_signal(self, 'mode_change', self.statusbar.set_text)
        #urwid.connect_signal(self, 'mode_change', self.show_args)

        alterBar = lambda bar, mode: self.statusbar.set_text(mode)
        urwid.connect_signal(self, 'mode_change', alterBar)

    def keypress(self, size, key):

        if self.mode == self.modes.NORMAL:
            raise urwid.ExitMainLoop()
        else:
            self.set_mode(self.modes.NORMAL)


fill = urwid.Filler( urwid.Edit("ass") )
wrap = vim_wrapper(fill)
loop = urwid.MainLoop(wrap)
loop.run()
#print(wrap.modes.NORMAL)

# TODO
# - Connect the statusbar widget to the event which changes modes.
