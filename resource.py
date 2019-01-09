import settings


class Resource:
    def __init__(self, pygame):
        self.img_background = pygame.image.load(settings.PATH_IMG_BACKGROUND).convert()
