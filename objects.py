class Lixo:

    # Iniciar com x, y, frame que a sacola foi gerada, largura do sprite, altura do sprite, id (ignorar por enquanto, é pra ser uma spritesheet dps)

    def __init__(self, pos_x, pos_y, frame_start, size_x, size_y, id):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.frame_start = frame_start
        self.size_x = size_x
        self.size_y = size_y
        self.id = id

    def x(self):
        return self.pos_x
    def y(self):
        return self.pos_y
    def startframe(self):
        return self.frame_start
    def sizex(self):
        return self.size_x
    def sizey(self):
        return self.size_y
    def sprite_id(self):
        return self.id

class Player:

    # O player por enquanto é só x, y, largura da imagem e altura da imagem

    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
    
    def x(self):
        return self.pos_x
    def y(self):
        return self.pos_y
    def sizex(self):
        return self.size_x
    def sizey(self):
        return self.size_y