import pygame
import pygame_textinput

import UI
import word_generator


def main():
    screen = UI.Screen()
    screen.setup()

    text_input = pygame_textinput.TextInput()
    text_input.set_text_color(screen.color_white)
    text_input.set_cursor_color(screen.color_white)

    active_words = [word_generator.Word(screen)]

    running = True
    running_frame = 0
    while running:
        screen.screen.fill(screen.color_black)

        if running_frame == 60:
            active_words.append(word_generator.Word(screen))
            running_frame = 0
        else:
            running_frame = running_frame + 1

        for i in active_words:
            screen.screen.blit(i.get_text(), i.get_text_rect())
        screen.screen.blit(text_input.get_surface(), (1100, 680))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if text_input.update(events):
            for i in active_words:
                if i.get_name() == text_input.get_text():
                    active_words.remove(i)
                    del i
                    break
            text_input.clear_text()

        for i in active_words:
            i.textRect = i.textRect.move(screen.speed)
            if i.textRect[0] >= 1280:
                print("Sorry you lost")
                pygame.quit()
                quit()

        screen.clock.tick(30)
        pygame.display.update()


pygame.init()
main()

