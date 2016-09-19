#!/usr/bin/env python
import urwid;

def key_handler(key):
    if key in('q', 'Q'):
        raise urwid.ExitMainLoop();

pallete = [ 
        ('I say', 'default,bold', 'default', 'bold'),
        ('I nay', 'default,italic', 'default', 'italic'),
    ];
question_asked = urwid.Edit( ("I say", "What's your name?\n") );
question_reply = urwid.Text("0");
#question_reply = urwid.Text( [("I nay", "Mesa "), ( "I say", "reply.")] );
#question_reply = urwid.Text( ("I say", "Mesa reply.") );
#question_reply = urwid.Text( "Mesa reply.");
region_divider = urwid.Divider("-");
testText = urwid.Text("Mesa test.");

button = urwid.Button( "Get Outta Here." );

pile = urwid.Pile( [
    question_asked,
    region_divider,
    question_reply,
    region_divider,
    button,
    testText,
    ] )

fill = urwid.Filler( pile, valign='middle' );

def exit_on_click(button):
    raise urwid.ExitMainLoop();

def on_change(edit, new_text):
    question_reply.set_text("Nice to meet you, {:s}".format(new_text) );

# Counts the number of total changes made to an edit box.
#def on_change(edit, new_text):
    #if question_reply.get_text()[0] == "":
        #question_reply.set_text("1");
    #else:
        #question_reply.set_text( str( int( question_reply.get_text()[0] ) + 1 ) );

#def on_change(edit, new_text):
    #testText.set_text( str(question_reply.get_text()) );

urwid.connect_signal( button, 'click', exit_on_click );
urwid.connect_signal( question_asked, 'change', on_change);

loop = urwid.MainLoop(fill, unhandled_input=key_handler);
loop.run();

"""

Text.get_text function:
    - Returns a tuple of the form:
    - 0: The actual text
    - 1: An array of tuples, each of the form:
        - ( {display_attribute}, {# of chars affected by display attribute} )
    - It seems that these tuples appear from left to right in the order that
      they appear in the string.

What events are there for use with 'urwid.connect_signal'? Is there a way to
get a list of events for each thing? Speaking of which, what things can we use?
Is it only widgets?
 
"""

