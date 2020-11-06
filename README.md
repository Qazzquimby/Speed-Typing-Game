# Speed-Typing-Game

As for now the application is in it's barebones. 
Only code present is to make the base logic of the game to work

### Questions:
- I am unsure as to if I am doing it right 
(probably no, since I am passing too many arguments around)
    - `self.game_logic = GameLogic(self.game_state.active_words, 
    self.game_state.running_frame, self.game_state.screen)`
    - problem is that the class GameLogic is using all of these 3, could send game_state as
    argument? but that way all of the other data would be sent, when it doesnt need it 
    (probably my game_state is not constructed properly?)
- I have seen a couple of different ways of people doing this, but whats the convention
for arguments and variables?
    - `def __init__(self, active_words, text_input):`
    
        `self.active_words = active_words`
        
        `self.text_input = text_input`
    - is how would you differentiate between the active_words argument and the self.active_words
- How to organize all the different classes created? When splitting the previous "Game" class.
Many classes were created (5 in this case).
    - Would all of these have files for them individually?
    - Should I create a folder and have all these classes inside the folder? (since they are
    "under" main)
- When doing the git status, I see two "modified" that I have no idea why they are there
    - `__pycache__/UI.cpython-37.pyc
    - `__pycache__/pygame_textinput.cpython-37.pyc

