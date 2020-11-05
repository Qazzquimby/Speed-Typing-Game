# Speed-Typing-Game

As for now the application is in it's barebones. Only code pressent is to make the base logic of the game to work

Questions:
  I am unsure as to what way of organizing the classes should I use.
    If a function (like the function "run_game") calls different functions (like it calling "draw_screen" and "event_handler"
      How do I organize those functions in the code?
      Do I add them by order of apperance? and if so, if those functions call other functions themselves (no occurrence of this at the moment of writing the code)
      How do I organize them? Would it be something like this?
      
        do_something()
          functionA()
          functionB()
          
        functionA()
          print("FunctionA")
          functionA1()
          
        functionA1()
          print("FunctionA1")
          
        functionB()
          print("FunctionB")
          
  I am unsure as what the common practices are for spacing on the code. specially inside functions
    For personal clarity I was used to put spaces between different smaller "chunks" of code inside the function (mostly because my functions where doing "too much")
    Now that I am trying to make everything cleaner and make smaller and smaller functions, I find myself with things like in main, Game.run_game() where you can find:
    (This looks wrong to me, specially since there is now more functions and they are separated by 1 line between them (as because of PEP8))
    
      def run_game()
        self.add_word_to_active_words()

        self.draw_screen()

        events = pygame.event.get()
        self.handle_events(events)
        ...
        
  I am unsure if I am doing it right. I am trying to become accostumed to work with github commits and all that jazz
    I have tried to put explanations on each of the commits I have put up. Do they look correct or there is something I am doing wrong?
    Also I have no idea what "Merge branch 'main' of... in the commits is.
