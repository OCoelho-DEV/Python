#Setter
class Pen:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        if value is None:
            raise ValueError("Color can't be None")
        
        self._color = value


p1 = Pen('Blue')
print(p1.color)
p1.color = "Pink"
# p1.color = None
print(p1.color)