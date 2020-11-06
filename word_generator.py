import random


class Word:
    
    def __init__(self, screen):
        self.words_available = ["chorus", "forecast", "exact", "virgin", "pest", "shot", "fly", "shame", "gift", 
                                "retain", "perfume", "atmosphere", "censorship", "looting", "banana", "face", "likely", 
                                "lily", "stamp", "biology"]

        self.name = self.generate_random_word()
        self.coordinates = self.generate_random_coordinates()
        self.text = screen.font.render(self.name, True, screen.color_white, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.coordinates

    def generate_random_word(self):
        return random.choice(self.words_available)
    
    def generate_random_coordinates(self):
        return 0, random.randint(50, 670)
