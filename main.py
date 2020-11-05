import pygame

import UI
import word_generator
import pygame_textinput


class Game:

    def __init__(self):
        self.screen = UI.Screen()
        self.text_input = pygame_textinput.TextInput()
        self.active_words = []
        self.running_frame = 0

    def setup_game(self):
        self.screen.setup()
        self.text_input.set_text_color(self.screen.color_white)
        self.text_input.set_cursor_color(self.screen.color_white)

    def run_game(self):
        running = True
        while running:
            self.add_word_to_active_words()

            self.draw_screen()

            events = pygame.event.get()
            self.handle_events(events)

            self.check_if_loss()

            self.screen.clock.tick(30)
            pygame.display.update()

    def add_word_to_active_words(self):
        if self.running_frame % 60 == 0:
            self.active_words.append(word_generator.Word(self.screen))
        self.running_frame += 1

    def draw_screen(self):
        self.screen.screen.fill(self.screen.color_black)

        for active_word in self.active_words:
            self.screen.screen.blit(active_word.get_text(), active_word.get_text_rect())
            active_word.textRect = active_word.textRect.move(self.screen.speed)
        self.screen.screen.blit(self.text_input.get_surface(), (1100, 680))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.text_input.update(events):
            for active_word in self.active_words:
                if active_word.get_name() == self.text_input.get_text():
                    self.active_words.remove(active_word)
                    del active_word
                    break
            self.text_input.clear_text()

    def check_if_loss(self):
        for active_word in self.active_words:
            if active_word.textRect[0] >= 1280:
                print("Sorry you lost")
                pygame.quit()
                quit()


def main():
    pygame.init()
    game = Game()
    game.setup_game()
    game.run_game()


if __name__ == '__main__':
    main()
