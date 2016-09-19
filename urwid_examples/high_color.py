#!/usr/bin/env python
import urwid;

# Practice switching from standard 16 colors to 256 colors in urwid.

def key_handler(key):
    if key in('q', 'Q'):
        raise urwid.ExitMainLoop();
    elif key in('p', 'P'):
        pile.contents.pop();

# significance of tuple entries, in order from left to right:
# 1. attribute name.
# 2. FG color for 16 color mode.
# 3. BG color for 16 color mode.
# 4. Monochrome mode settings.
# 5. FG color for 256 color mode.
# 6. BG color for 256 color mode.
pallete = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'),
]

placeHolder = urwid.AttrMap( urwid.SolidFill('-'), 'bg');
loop = urwid.MainLoop(placeHolder, pallete, unhandled_input=key_handler);
loop.screen.set_terminal_properties(colors=256);
loop.widget.original_widget =  urwid.Filler( urwid.Pile([]) );

print(loop.widget); # Returns the AttrMap.
print(loop.widget.original_widget); # Returns the Filler within the AttrMap
print(loop.widget.base_widget); # Returns the Pile within the Filler.
print(loop.widget.original_widget.original_widget); # Returns the Pile within the Filler.

#placeHolder = urwid.SolidFill();
#loop = urwid.MainLoop(placeHolder, pallete, unhandled_input=key_handler);
#loop.screen.set_terminal_properties(colors=256);
#loop.widget = urwid.AttrMap(placeHolder, 'bg');
#loop.widget.original_widget =  urwid.Filler( urwid.Pile([]) );

div = urwid.Divider('-');
outside = urwid.AttrMap(div, 'outside');
inside = urwid.AttrMap(div, 'inside');
txt = urwid.Text( ('banner', u' Hello World'), align='center');
streak = urwid.AttrMap(txt, 'streak');
pile = loop.widget.base_widget;

for item in [outside, inside, streak, inside, outside]:
    pile.contents.append( (item, pile.options() ) );
loop.run();

"""
 - Q: How exactly does text get placed in a solidfill? Does urwid read the
   dimensions of the terminal? If so, when? Is it upon creating the SolidFill
   object, or is upon creating the loop object? My hunch is the latter, since
   the loop object seems to have a 'screen' property. I imagine that this
   property might carry other information about the state of the screen, such
   as the screen dimension.
 - Q: Why is it that we need the placeholder in the first place?
    - It looks like the major reason is the following lines: placeHolder =
      urwid.AttrMap( urwid.SolidFill('_'), 'bg'); loop.widget.orignal_widget =
      urwid.Filler( urwid.Pile([]) ); The 1st line makes the placeholder part
      of an attribute map. It's been wrapped in it now. The second line
      replaced the wrapped widget of the attribute map. So by using the
      placeholder, we're able to:
      - Create the loop object that we know that we want to use, before we've
        finished building everything.
      - Apply the attribute map to the widget that we eventually want to
        actually use.  It seems that I might've been onto something with the
        CSS comparison, because the point of this is to be able to build the
        GUI from the top to the bottom, starting with the larger enclosing
        elements, then building the smaller ones. Using the placeholder allows
        us to work with the largest element while we build the smaller elements
        that the placeholder will contain.
  - Q: What exactly is going on with the 'base_widget' property from the
    following line?  pile = loop.widget.base_widget;
    - I think that what's happening there is we're taking the pile that we
      defined earlier, meaing that we can now add stuff to it. It's not a copy
      of that thing, or just another thing of that type: it's the actual widget
      that's being used. The part that I'm not clear on yet is why the use of
      'base_widget' instead of something like 'widget' or 'original_widget'.
    - Wait the reason for the 'base_widget' thing might be to retrieve the
      'Pile', and not the 'Filler'.



"""


