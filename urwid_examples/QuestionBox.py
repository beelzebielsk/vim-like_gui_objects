import urwid;

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
            urwid.emit_signal(self, 'enter', self);
            try:
                self.set_caption( next( self.questions ) + '\n' );
                self.set_edit_text("");
            except StopIteration:
                # Passing the whole thing so that something else can
                # decide what to do with it once it's finished.
                urwid.emit_signal(self, 'finish', self);
