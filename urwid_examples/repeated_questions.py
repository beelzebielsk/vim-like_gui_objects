#!/usr/bin/env python
import urwid;
import QuestionBox;

def questions():
    while True:
        yield "What's your name?";


qIt = questions();
box = QuestionBox.Questions(qIt);
pile = urwid.Pile([box]);
container = urwid.Filler(pile);
loop = urwid.MainLoop(container);

def onAnswer(questionBox):
    response = "Nice to meet you, {0}".format;
    if questionBox.answers[-1].lower () == "quit":
        raise  urwid.ExitMainLoop();
    newContents = [ 
        ( urwid.Text( 
            #'\n'.join([questionBox.get_text()[0].split('\n')[0], questionBox.edit_text])
            questionBox.get_text()[0]
        ), pile.options() ),
        ( urwid.Text( response( questionBox.edit_text ) ), pile.options() ),
        ( urwid.Divider(), pile.options() ),
    ]
    pile.contents[-1:-1] = newContents;

urwid.connect_signal(box, 'enter', onAnswer);
loop.run();

#print(QuestionBox);
#print( dir() );
#print( dir(urwid) );
#print( dir(QuestionBox) );
