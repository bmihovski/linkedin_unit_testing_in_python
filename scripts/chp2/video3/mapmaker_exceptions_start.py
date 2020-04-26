
class Point():
    def __init__(self, name, latitude, longitude):
        if not isinstance(name, str):
            raise ValueError("Invalid city name type")
        self.name = name
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination")
        self.latitude = latitude
        self.longitude = longitude


    def get_lat_long(self):
        return (self.latitude, self.longitude)


class Map():
    def __init__(self):
        self.__collection = list()

    @property
    def maps(self):
        return self.__collection

    @maps.setter
    def maps(self, point):
        self.__collection.append(point)

    def is_point_present(self, point):
        if not point in self.__collection:
            raise ValueError("Point not found")
        else:
            return True
