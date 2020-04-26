class Point():
    def __init__(self, name: str, lat: float, longt: float):
        self.__name = name
        self.__lat = lat
        self.__longt = longt

    def get_lat_long(self):
        return (self.__lat, self.__longt)
