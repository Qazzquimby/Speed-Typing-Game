import random
from points import Point

POSSIBLE_WORDS = ["chorus", "forecast", "exact", "virgin", "pest", "shot", "fly", "shame", "gift",
                  "retain", "perfume", "atmosphere", "censorship", "looting", "banana", "face", "likely",
                  "lily", "stamp", "biology"]


def _generate_random_word():
    return random.choice(POSSIBLE_WORDS)


def _generate_random_coordinates(screen_y_size):
    padding = 50
    min_spawn_y = 0 + padding
    max_spawn_y = screen_y_size - padding
    return Point(x=0, y=random.randint(min_spawn_y, max_spawn_y))


def spawn_random_word(screen_y_size):
    name = _generate_random_word()
    coordinates = _generate_random_coordinates(screen_y_size)
    return Word(name, coordinates)


class Word:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
