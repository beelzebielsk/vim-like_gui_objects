#!/usr/bin/env python
import urwid;

# Quit by pressing any key once the main question list is exhausted.  It'll
# quit automatically because, once the main question list is exhausted, the
# 'edit' widget disappears, being replaced by a plain 'Text" widget. This
# widget doesn't really handle keypresses, so all keypresses will be counted as
# unhandled, and therefore quit the program.
def key_handler(key):
    #if key in('q', 'Q'):
        #raise urwid.ExitMainLoop();
    raise urwid.ExitMainLoop();

pallete = [
        ('question', 'light gray,bold', 'black', 'bold'),
        ('top', 'white', 'dark gray', 'bold'),
        ('bottom', 'dark gray', 'white', 'bold'),
]

questions = [
        "What's your first name?",
        "What's your last name?",
        "How old are you?",
        "What state do you live in?",
        "What city do you live in?",
        "What's your zip code?",
]

class Questions(urwid.Edit):

    # The widget that 'self' will replace itself with
    # once the list of questions have been exhausted.
    # Somehow, despite this statement, the 'change' event is automatically
    # added to signals.
    signals = ['finish', 'enter'];

    # Constructor.
    # Questions is an iterator of strings.
    def __init__(self, questions, finishText='Thank you for answering my questions.'):
        # Call parent constructor. Have it do everything that it
        # does. Sets up first question.
        #super(Questions, self).__init__( questions[0] + '\n' );
        super().__init__( next( questions ) + '\n' );

        # Make an iterator of the questions, so that
        # switching questions is easy. Downfall is that
        # inserting questions at beginning will probably
        # never work, but appending questions should.
        #self.questions = iter(questions[1:]);
        self.questions = questions;
        self.answers = [];
        self.finishedText = finishText;

    def keypress(self, size, key):
        if key != 'enter':
            return super(Questions, self).keypress(size, key);
        else:
            text = self.base_widget.get_text()[0];
            answer = text.split('\n')[1];
            self.answers.append( answer );
            urwid.emit_signal(self, 'enter', answer);
            try:
                self.set_caption( next( self.questions ) + '\n' );
                self.set_edit_text("");
            except StopIteration:
                urwid.emit_signal(self, 'finish', self.answers);
                topPile.contents.pop();
                topPile.contents.append( 
                        ( urwid.Text(self.finishedText), topPile.options() ) 
                );

# Somehow, even without this statement, the signals fire off just fine.
#urwid.register_signal(Questions, ['finish', 'enter']);

# Callback for calling every time a new answer is typed.
def updateAnswerList(answer):
    bottomPile.contents.append( ( urwid.Text(answer), bottomPile.options() ) );

# Callback for calling once the question list is fully exhausted.
def spellOutAddress(answers):
    bottomPile.contents.clear();
    address = urwid.Text( "Address:\n{0} {1}\n{4}, {3} {5}\n".format(*answers) );
    bottomPile.contents.append( (address, bottomPile.options() ) );

#print( Questions.__mro__ );
#print("Original Widget:",  Questions.original_widget ); #Doesn't Exist.
#print("Base Widget:",  Questions.base_widget );

# Splits screen into a top pile, where the questions are asked,
# and a bottom pile, where responses are displayed.
# 'mainPile' holds all the pieces of the screen, where the topPile
# is the first element of the mainPile, then there's 'divider'
# element which splits the screen, then there's the 'bottomPile'
# which is the last element, and holds all of the Text widgets that
# imply responses.
mainPile = urwid.Pile([]);
container = urwid.Filler( mainPile, valign='top' );
divider = urwid.Divider('-');
 
topPile = urwid.Pile([]);
questionSeries = Questions( iter(questions) );
topPile.contents.append(  ( questionSeries, topPile.options() ) );
bottomPile = urwid.Pile([]);

mainPile.contents.append( ( topPile, mainPile.options() ) );
mainPile.contents.append( ( divider, mainPile.options()) );
mainPile.contents.append( ( bottomPile, mainPile.options() ) );

# Connects the callbacks for these signals to the signals themselves.
# They'll now be called when the 'questionSeries' object emits the
# respective signals.
urwid.connect_signal(questionSeries, 'enter', updateAnswerList);
urwid.connect_signal(questionSeries, 'finish', spellOutAddress);

loop = urwid.MainLoop(container, pallete, unhandled_input=key_handler);
loop.run();

# For figuring out what signals the object can handle.
#print(Questions.signals);
