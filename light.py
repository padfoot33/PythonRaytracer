from color import Color

class Light:
    """Light Represents a point light source of certain color"""
    def __init__(self,position,color = Color.from_hex("ffffff")):
        self.position = position
        self.color = color