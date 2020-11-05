import random


class Word:
    
    def __init__(self, screen):
        self.words_available = ["chorus", "forecast", "exact", "virgin", "pest", "shot", "fly", "shame", "gift", 
                                "retain", "perfume", "atmosphere", "censorship", "looting", "banana", "face", "likely", 
                                "lily", "stamp", "biology"]

        self.name = self.generate_random_word()
        self.coordinates = self.generate_random_coordinates()
        self.text = screen.font.render(self.get_name(), True, screen.color_white, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.get_coordinates()

    def generate_random_word(self):
        return random.choice(self.words_available)
    
    def generate_random_coordinates(self):
        return 0, random.randint(50, 670)

    def get_name(self):
        return self.name

    def get_coordinates(self):
        return self.coordinates

    def get_text(self):
        return self.text

    def get_text_rect(self):
        return self.textRect
