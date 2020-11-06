import pygame

import UI
import word_generator
import pygame_textinput

from points import Point


class GameState:

    def __init__(self):
        self.text_input = pygame_textinput.TextInput()
        self.active_words = []
        self.running_frame = 0


class GameGraphics:
    def __init__(self, state, screen):
        self.state = state
        self.screen = screen
        self.screen.setup()

        self.state.text_input.set_text_color(self.screen.color_white)
        self.state.text_input.set_cursor_color(self.screen.color_white)

    def update(self):
        self.screen.screen.fill(self.screen.color_black)
        self.draw_words()
        self.print_texts()

    def draw_words(self):
        for active_word in self.state.active_words:
            active_word.text = self.screen.font.render(active_word.name, True, self.screen.color_white, None)
            active_word.textRect = active_word.text.get_rect()
            active_word.textRect.center = tuple(active_word.coordinates)

            self.screen.screen.blit(active_word.text, active_word.textRect)

    # Is just a one liner, but when there is more text to print (like the words per minute etc)
    # this function will take coordinates and the text to print, so this can be used for all texts
    def print_texts(self):
        self.screen.screen.blit(
            self.state.text_input.get_surface(),
            (self.screen.size.x - 200, self.screen.size.y - 50))


class GameLogic:

    def __init__(self, state, size):
        self.state = state
        self.size = size

        self.word_speed = Point(2, 0)

    def update(self):
        self.move_active_words()
        self.add_word_to_active_words()
        self.check_if_loss()
        self.state.running_frame += 1

    def move_active_words(self):
        for active_word in self.state.active_words:
            active_word.coordinates += self.word_speed

    def add_word_to_active_words(self):
        if self.state.running_frame % 60 == 0:
            self.state.active_words.append(word_generator.spawn_random_word(self.size.y))

    def check_if_loss(self):
        for active_word in self.state.active_words:
            if active_word.coordinates.x >= self.size.x:
                print("Sorry you lost")
                pygame.quit()
                quit()


class GameEventHandler:

    def __init__(self, state):
        self.state = state

    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.state.text_input.update(events):
            for active_word in self.state.active_words:
                if active_word.name == self.state.text_input.get_text():
                    self.state.active_words.remove(active_word)
                    del active_word
                    break
            self.state.text_input.clear_text()


class GameLoop:

    def __init__(self, state, graphics, logic, events):
        self.game_state = state
        self.game_graphics = graphics
        self.game_logic = logic
        self.game_events_handler = events

    def run_game(self):
        running = True
        while running:
            self.game_logic.update()

            self.game_graphics.update()

            events = pygame.event.get()
            self.game_events_handler.update(events)

            self.game_graphics.screen.clock.tick(30)
            pygame.display.update()


def main():
    # config options. Can be moved elsewhere, or even read from a file.
    SCREEN_DIMENSIONS = Point(x=1280, y=720)

    pygame.init()

    state = GameState()

    screen = UI.Screen(SCREEN_DIMENSIONS)
    graphics = GameGraphics(state, screen)

    logic = GameLogic(state, SCREEN_DIMENSIONS)
    events = GameEventHandler(state)

    loop = GameLoop(state=state, graphics=graphics, logic=logic, events=events)

    loop.run_game()


if __name__ == '__main__':
    main()
