import pygame

import UI
import word_generator
import pygame_textinput


class GameState:

    def __init__(self):
        self.screen = UI.Screen()
        self.screen.setup()
        self.text_input = pygame_textinput.TextInput()
        self.text_input.set_text_color(self.screen.color_white)
        self.text_input.set_cursor_color(self.screen.color_white)
        self.active_words = []
        self.running_frame = 0
        self.word_speed = (2, 0)


class GameGraphics:
    def __init__(self, state):
        self.screen = state.screen
        self.text_input = state.text_input
        self.active_words = state.active_words
        self.word_speed = state.word_speed

    def update(self):
        self.screen.screen.fill(self.screen.color_black)
        self.move_words()
        self.print_texts()

    def move_words(self):
        for active_word in self.active_words:

            active_word.text = self.screen.font.render(active_word.name, True, self.screen.color_white, None)
            active_word.textRect = active_word.text.get_rect()
            active_word.textRect.center = active_word.coordinates

            self.screen.screen.blit(active_word.text, active_word.textRect)
            active_word.coordinates = tuple(orig + move for orig, move
                                            in zip(active_word.coordinates, self.word_speed))

    # Is just a one liner, but when there is more text to print (like the words per minute etc)
    # this function will take coordinates and the text to print, so this can be used for all texts
    def print_texts(self):
        self.screen.screen.blit(self.text_input.get_surface(), (self.screen.X_size - 200, self.screen.Y_size - 50))


class GameLogic:

    def __init__(self, active_words, running_frame, screen):
        self.active_words = active_words
        self.running_frame = running_frame
        self.screen = screen

    def update(self):
        self.add_word_to_active_words()
        self.check_if_loss()

    def add_word_to_active_words(self):
        if self.running_frame % 60 == 0:
            self.active_words.append(word_generator.Word())
        self.running_frame += 1

    def check_if_loss(self):
        for active_word in self.active_words:
            if active_word.coordinates[0] >= self.screen.X_size:
                print("Sorry you lost")
                pygame.quit()
                quit()


class GameEventHandler:

    def __init__(self, active_words, text_input):
        self.active_words = active_words
        self.text_input = text_input

    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.text_input.update(events):
            for active_word in self.active_words:
                if active_word.name == self.text_input.get_text():
                    self.active_words.remove(active_word)
                    del active_word
                    break
            self.text_input.clear_text()


class GameLoop:

    def __init__(self):
        self.game_state = GameState()
        self.game_graphics = GameGraphics(self.game_state)
        self.game_logic = GameLogic(self.game_state.active_words, self.game_state.running_frame, self.game_state.screen)
        self.game_events_handler = GameEventHandler(self.game_state.active_words, self.game_state.text_input)

    def run_game(self):
        running = True
        while running:
            self.game_logic.update()

            self.game_graphics.update()

            events = pygame.event.get()
            self.game_events_handler.update(events)

            self.game_state.screen.clock.tick(30)
            pygame.display.update()


def main():
    pygame.init()
    game = GameLoop()
    game.run_game()


if __name__ == '__main__':
    main()
