#!/usr/bin/env python
import urwid;

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

answers = [];

#class QuestionsBox(urwid.Filler):
    #def __init__(self, questions):
        #super(QuestionsBox, self).__init__( urwid.Edit(questions[0]) );
        #self.questions = iter(questions[1:]);
        #self.answers = [];
#
    #def keypress(self, size, key):
        #if key != 'enter':
            #return super(QuestionsBox, self).keypress(size, key);
        #else:
            #text = self.base_widget.get_text()[0];
            #answer = text.split('\n')[1];
            #self.answers.append( answer );
            #self.original_widget = urwid.Edit( self.questions.next() + '\n' );

class Questions(urwid.Edit):

    finishedText = \
        urwid.Text("Thanks for answering! Press any key to exit.");

    def __init__(self, questions):
        super(Questions, self).__init__( questions[0] + '\n' );
        self.questions = iter(questions[1:]);
        self.answers = [];

    def keypress(self, size, key):
        if key != 'enter':
            return super(Questions, self).keypress(size, key);
        else:
            text = self.base_widget.get_text()[0];
            answer = text.split('\n')[1];
            self.answers.append( answer );
            try:
                self.set_caption( next( self.questions ) + '\n' );
                self.set_edit_text("");
            except StopIteration:
                topPile.contents.pop();
                topPile.contents.append( (self.finishedText, topPile.options() ) );

#print( Questions.__mro__ );
#print("Original Widget:",  Questions.original_widget ); #Doesn't Exist.
#print("Base Widget:",  Questions.base_widget );
mainPile = urwid.Pile([]);
container = urwid.Filler( mainPile, valign='top' );
divider = urwid.Divider('-');
 
#topPile = urwid.Pile([ QuestionsBox(questions) ]);
topPile = urwid.Pile([]);
topPile.contents.append(  ( Questions(questions), topPile.options() ) );
#print( QuestionsBox.__mro__ );
bottomPile = urwid.Pile([]);

mainPile.contents.append( ( topPile, mainPile.options() ) );
mainPile.contents.append( ( divider, mainPile.options()) );
mainPile.contents.append( ( bottomPile, mainPile.options() ) );

#container = QuestionBox( urwid.Edit( ('question', questions[0] + '\n' ) ) );
loop = urwid.MainLoop(container, pallete, unhandled_input=key_handler);
loop.run();
