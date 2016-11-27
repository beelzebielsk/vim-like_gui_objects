#!/usr/bin/env python
import urwid;

def key_handler(key):
    if key in('q', 'Q'):
        raise urwid.ExitMainLoop();

keyHolder = []; #DEBUG.
# This was for gathering the keypresses for studying them.

# Defines class QuestionBox which inherits from urwid.Filler.
class QuestionBox(urwid.Filler):

    # Defines (overrrides, actually) a function 'keypress' for
    # all QuestionBox objects, which accepts the arguments 'size'
    # and 'key'.
    # TODO: What is size used for?
    def keypress(self, size, key):
        if key != 'enter':
            # If the key is not enter, then call the keypress
            # function of a Base Class, which is urwid.Filler.keypress.
            # What does this return?
            # Apparently nothing. I suppose that's just a way of ending
            # that function call and calling the super function in one
            # line. Note that, since the function is called twice, the
            # keys get entered twice.
            keyHolder.append( super(QuestionBox, self).keypress(size, key) );
            return super(QuestionBox, self).keypress(size, key);

        # Considering that this inherits from urwid.Filler, the
        # value of original_widget is probably the widget that
        # this decorator decorates, which would be the 'Edit'
        # widget.
        self.original_widget = urwid.Text(
            "Yeah, no one gives a shit. Just press 'Q' and get out my face, {!r}."
            .format(edit.edit_text) )

edit = urwid.Edit("What's your name?\n");
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=key_handler);
loop.run();

# print (*keyHolder, sep=", ");
# They all return 'None'. I suppose that the keypress function doesn't actually return anything.

#print(QuestionBox.__mro__);
# Prints: QuestionBox, then urwid.Filler, then urwid.decoration.WidgetDecoration, then urwid.widget.Widget, then object.

# Once again, we can't pass the edit object directly to the main loop. We have
# to pass a filler object.

# How does the urwid.Filler.keypress function work? Perhaps it just passes it
# to it's base widget, since the filler class seems to be mainly about
# containment and decoration?

print(str(urwid.Filler.keypress) );
