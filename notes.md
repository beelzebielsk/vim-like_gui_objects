- Don't make a bunch of specialized widgets. Not necessary. Make a
  widget wrapper with a keypress function. When in normal mode, it'll
  handle navigation. When in 'insert' mode, it'll pass keys straight to
  underlying (focused) widgets.
- Focus mainly on navigation, and mode switching. Maybe even
  extensibility.
- There's a bunch of functions that won't make sense in every context,
  but will make sense in some contexts. Just leave those open and allow
  other people to easily define them when they need to.
- In piles, keypresses seem to go to the pile first. The keypress is
  sent to the in focus element from there. The in focus element is
  supposed to, from there, handle the key, or return it back so that the
  pile can process it.

# Command Maps

## What has them?

It's looking like selectables have command maps, and you can access them
through the `_command_map` field.

- Buttons
- ListBoxes

## How do They Work?

The command map doesn't call functions. It's just used to determine what
a key is meant to do.

So when defining a keypress function, you could make statements like:

  if command_map[key] == 'command'
	perform command

Or, even better:

  if command_map[key] in [ ...list of possible commands... ]
	{handle said commands}

You can separate mappings from controls using this.

# Good Vim Stuff To Include

- Numbers before commands
- Modes (insert, normal)
  - Optionally visual, for copying the contents of certain boxes.
  - Consider defining a 'yield' for these boxes which controls how
	things come out of the boxes for copying and pasting.

# TODO

- Read up on the global command table of urwid. See if you can link that
  to the vim command thing that you've got going on, and see if it's
  possible to change it at all, or that would be wise.
- Check the way that urwid widgets tend to handle unhandled keys:
  - When do they call super methods?
	- I think the `super` methods is specifically for when you've
	  inherited from a widget and you want to lean on that widget's
	  functionality when your customizations don't handle it.
  - When do they just return the key?
	- This is probably for when the current widget completely does not
	  handle the key in any way: neither it, nor any class from which it
	  inherits.
