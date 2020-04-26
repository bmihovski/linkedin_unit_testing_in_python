class User:
    def __init__(self, height, color):
        super().__init__()
        self.__height = height
        self.__color = color

    @property
    def color(self):
        return self.__color

    def reward(self):
        if self.__height < 156:
            return "candy bar"
        elif 156 == self.__height < 186:
            return "candy stick"
        else:
            return "hard candy"
