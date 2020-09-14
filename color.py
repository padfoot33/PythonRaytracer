from Vector import Vector

class Color(Vector):
    """Stores Color as RGB Triplets, alias for vector"""

    @classmethod
    def from_hex(cls,hexColor = "#000000"):
        x = int(hexColor[1:3],16)/255.0
        y = int(hexColor[3:5],16)/255.0
        z = int(hexColor[5:7],16)/255.0
        return cls(x,y,z)
        