from constants import *

class LongTextWriter(pygame.sprite.Sprite):

    def __init__(self, long_text, font='arial', size=14, color='white', width=300):
        super().__init__()
        self.text = long_text
        self.font = pygame.font.SysFont(font, size)
        self.size = size
        self.width = width + 100
        self.color = color
        self.line_height = size + 6
        self.line_width = width
        self.line = 0
        self.rendered_group = []

    def update(self):
        self.render_long_text()
        self.image = pygame.Surface((self.width, self.line_height*self.line), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.blits(self.rendered_group)

    def render_long_text(self):
        all_words = self.text_to_words(self.text)

        current_line = ""
        for word in all_words:
            current_line += word + " "
            if self.font.size(current_line)[0] > 300:
                self.render_line(current_line)
                current_line = ""
        self.render_line(current_line)

    def text_to_words(self, long_text: str):
        all_lines = long_text.splitlines()
        all_words = []
        for line in all_lines:
            all_words.extend(line.strip().replace('\n', ' ').split())
        return all_words

    def render_line(self, line_to_render):
        rendered = self.font.render(line_to_render, True, self.color)
        position = rendered.get_rect()
        position.centerx = self.width/2
        position.y = self.line * self.line_height
        self.rendered_group.append((rendered, position))
        self.line += 1 