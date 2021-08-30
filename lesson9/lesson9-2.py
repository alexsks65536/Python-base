class Road:
    def __init__(self, length, width):
        
        self._length = length
        self._width = width

    def do_road_profile(self, weight=25, layer=5):
        return f"{self._length} м * {self._width} м * {weight} кг * {layer} см =" \
               f"{(self._length * self._width * weight * layer) / 1000} т"

way = Road(8000, 10)
print(way.do_road_profile())