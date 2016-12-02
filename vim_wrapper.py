#!/usr/bin/env python

import urwid

class vim_statusbar(urwid.WidgetWrap):
    def __init__(self, debug=False):
        self.debug = debug
        self.statusBox = urwid.Text("A")
        self.keyBuffer = urwid.Text("")
        container = urwid.Columns([self.statusBox, self.keyBuffer])
        urwid.WidgetWrap.__init__(self, container)
        if self.debug:
            self.debug_box = urwid.Text("")
            self._w.contents.append( \
                (self.debug_box, self._w.options()  )
            )

    def set_status(self, newStatus):
        self.statusBox.set_text(newStatus)

    # Will not cause problems if not in debug mode.
    def set_debug_box(self, text):
        if not self.debug:
            return
        self.debug_box.set_text(text)

# Consider just overriding the keypress function of whatever widget that
# this is passed, and doing only vim-like stuff during normal mode, and
# otherwise passing the keypresses straight into the wrapped widget
# otherwise.
class vim_wrapper(urwid.WidgetWrap):
    class modes():
        NORMAL = 'NORMAL'
        INSERT = 'INSERT'

    signals = ['mode_change']
    _selectable = True

    normal_bindings = {
        'j' : 'cursor down',
        'J' : 'cursor page down',
        'k' : 'cursor up',
        'K' : 'cursor page up',
        'h' : 'cursor left',
        '0' : 'cursor max left',
        'l' : 'cursor right',
        '$' : 'cursor max right',
        'i' : 'INSERT',
        'Z' : 'exit program',
    }

    insert_bindings = {}

    def set_mode(self, mode):
        self.mode = mode
        self._emit('mode_change', self.mode)

    def show_args(*args):
        print(*args, sep='\n')

    def __init__(self, widget):
        self.statusbar = vim_statusbar(debug=True)
        #alterBar = lambda bar, mode: self.statusbar.set_text(mode)
        alterBar = lambda bar, mode: self.statusbar.set_status(mode)
        urwid.connect_signal(self, 'mode_change', alterBar)
        self.set_mode(self.modes.NORMAL)

        urwid.WidgetWrap.__init__(self, urwid.Frame(widget, footer=self.statusbar) )


        # Establish command map for this, and a reverse map for the
        # wrapped container, which allows the wrapper to pass necessary
        # keys to wrapped container to achieve desired effects.
        self.normal_map = urwid.CommandMap().copy()
        self.normal_map._command = self.normal_bindings
        self._command_map = self.normal_map
        self.reverse_map = {}
        for k, v in self._w._command_map._command.items():
            self.reverse_map.update( [(v, k)] )
        #print(self.reverse_map)

    def keypress(self, size, key):

        # TODO: Handle situation when widget uses 'esc' key.
        if self.mode == self.modes.INSERT:
            if key == 'esc':
                self.set_mode(self.modes.NORMAL)
                return
            self._w.keypress(size, key)
        elif self.mode == self.modes.NORMAL:
            # Temporary: To pass 'esc' down to underlying container.
            if key == 'esc':
                self._w.keypress(size, key)
                return
            # If not a valid command.
            if key not in self._command_map._command:
                #self._w.keypress(size, key)
                return
            command = self._command_map[key]
            self.statusbar.set_debug_box(command) #DEBUG
            if command == self.modes.INSERT:
                self.set_mode(self.modes.INSERT)
            elif command == 'exit program':
                raise urwid.ExitMainLoop()
            else:
                key_for_command = self.reverse_map[command]
                self.statusbar.set_debug_box(key_for_command)
                self._w.keypress(size, key_for_command)


fill = urwid.Filler( urwid.Edit("ass"), height=('relative', 100) )
fill.original_widget = \
        urwid.Columns( [urwid.ListBox( [urwid.Edit("ass")]*10 )]*2 )
wrap = vim_wrapper(fill)
loop = urwid.MainLoop(wrap)
print(wrap._command_map._command)
loop.run()

# TODO
# - Connect the statusbar widget to the event which changes modes.
