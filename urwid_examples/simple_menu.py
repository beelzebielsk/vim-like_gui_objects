#!/usr/bin/env python
import urwid

choices = "ck gervais chapelle rock norton maron o'neal".split()

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for choice in choices:
        button = urwid.Button(choice);
        urwid.connect_signal(button, 'click', item_chosen, choice)
        body.append(button)
    # Both work. The default is 'SimpleFocusListWalker'.
    #return urwid.ListBox( urwid.SimpleFocusListWalker(body) )
    return urwid.ListBox( body )


def item_chosen(button, choice):
    response = urwid.Text(['You chose {}'.format(choice), '\n'])
    done = urwid.Button("Piss off")
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response, done]))

def exit_program(button):
    raise urwid.ExitMainLoop()

# I assume the 'left' and 'right' keyword arguments are margin sizes.
main = urwid.Padding(menu("Comedians", choices), left=2, right=2)
urwid.MainLoop(main).run()

# Arguments here:
# - Widget : The widget that will be emitting the event.
# - String : The name of the event to register the function with.
# - Function : The function to register with the event.
# - Stuff : Extra Data to send with the signal to the registered
#   function. At the minimum, it seems that the widget that emitted the
#   event will be sent as data, too.
#urwid.connect_signal(button, 'click' item_chosen, choice)
