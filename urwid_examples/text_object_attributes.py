#!/usr/bin/env python
import urwid;

def key_handler(key):
    if key in('q', 'Q'):
        raise urwid.ExitMainLoop();
    #txt.set_text(repr(key))
    txt.set_text(key)

pallete = [
        ('banner', 'black', 'light gray'),
        ('streak', 'black', 'dark red'),
        ('bg', 'black', 'dark blue'),
        ]

# This causes: 
# - the words "Hello World" to be displayed using the 'banner' pallete
# - the whitespace within the same row as "Hello World" to be displayed using
#   the 'streak' pallete.
# - The filler whitespace on the screen to be displayed using the 'bg' pallete.
#txt = urwid.Text( ('banner', u"Hello World"), align='left' );
#map1 = urwid.AttrMap(txt, 'streak');
#map1 = urwid.AttrMap(map1, 'bg');
#fill = urwid.Filler(map1, 'top');
#map2 = urwid.AttrMap(fill, 'bg');
#loop = urwid.MainLoop(map2, pallete, unhandled_input=key_handler);
#loop.run();

#txt = urwid.Text( ('streak', u"Hello World"), align='left' );
#txt = urwid.Text(u"Hello World", align='left' );
#fill = urwid.Filler(txt, 'top');
#map1 = urwid.AttrMap(fill, 'banner');
#loop = urwid.MainLoop(map1, pallete, unhandled_input=key_handler);
#loop.run();

#txt = urwid.Text("Hello World");
#fill = urwid.Filler(txt);
#loop = urwid.MainLoop(fill, unhandled_input=key_handler);
#loop.run();

txt = urwid.Text( ('banner', u"Hello World"), align='left' );
#txt = urwid.Text(u"Hello World", align='left' );
fill = urwid.Filler(txt, 'top');
map1 = urwid.AttrMap(fill, 'bg');
loop = urwid.MainLoop(map1, pallete, unhandled_input=key_handler);
loop.run();

""" So, 'AttrMap' objects accept 'Text' objects, and some other attribute or
something """

""" Apparently, whatever that extra argument is (I suppose the attribute), you
can enter whatever you want. There are no invalid entries. How does that work?
"""

""" So, thus far, the 'Filler' method, or constructor, can accept both an
'AttrMap' object and a 'Text' object. Either that, or these methods aren't
constructors, and they're passing the same or similar objects, or objects that
all come from a similar base class taht the 'Filler' method accepts.  """

# Note that the AttrMap methods refer to names that are in the 'pallete' array.

""" It might be more accurate to say that the tuples contained in the
'pallete' array are lists of attributes or something, and AttrMap method calls
somehow apply these attributes to the correc things. Either that, or they just
attatch 'tags' like 'banner', 'streak', and 'bg' onto certain things, which
allows the 'loop' method to use the entries in the tuples of the 'pallete'
array appropriately.  """

""" So, it seems that, once the 'txt' object is created, you've got the actual
text which has the display attribute 'banner', then you've got all of the
other stuff """

""" Why does trying to run the main loop with a plain textwidget object, as
opposed to a fill object, causes an error?  """

"""
- Q: Why does trying to run the main loop with an AttrMap applies to a filler
  object cause an error?
- A: It doesn't. I just fucked up.  
"""

""" I think I'm kinda getting it. If you specify a display attribute with a
text object, then that attribute gets applied to all of the text that you
explicitly typed out. any filler characters that you didn't specify are left
without an attribute. This could be fine if that's what you want. If that's not
what you want, you can use the AttrMap function to map a display attribute onto
all the text in a textobject that doesn't currenly have a display object.  """

""" As an example:
 - Giving the text 'Hello World' the banner display attribute, where that
   attribute has foreground color 'black' and background color 'light gray'
   associated with it through the 'pallete' array, causes the letters in 'Hello
   World' to be black, and causes the rectangles that contain those letters to
   have the background color 'light gray'.
 - Mapping the 'banner' attribute onto the whole text object `urwid.Text(
   ('banner', 'Hello World') )` causes all the letters to be black, and causes
   all the rectangles that contain the letters to be 'light gray'. It also
   causes the rectangles that contain any filler characters that are part of
   that text object to also be 'light gray'.
 - Mapping the 'banner' attribute onto a 'Filler' object that contains the
   whole text object would cause all of the previous changes (black letters and
   light gray background in all text cells, and filler cells for that one text
   widget), and cause those changes to be applies to all filler characters
   within the 'Filler' object. This means that the background of the entire
   screen would become light gray.  
 - Note that, if different display attributes were mapped onto these objects
   than 'banner', the effects of banner on enclosed objects wouldn't be
   cancelled out. The 'AttrMap' function only causes text which doesn't have a
   displayAttribute mapped onto it to have that display attribute mapped onto
   it.  In some sense, it's slightly similar to what CSS does, in that the most
   specific rules apply, and you can sort of cascade attributes down by placing
   them onto enclosing containers. However, rather than just specify rules from
   the top down, you have to apply the rules manually to a certain object, and
   have the rules 'tricle down' within text contained in the object which
   doesn't already have a rule applied to it.  """
