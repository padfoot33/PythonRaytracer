from color import Color

class Material:
    """Material has color and properties to react with light"""

    def __init__(self,color = Color.from_hex("#ffffff"),ambient = 0.05, diffuse = 1.0,
     specular = 1.0,reflection=0.5):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self,pos):
        return self.color

class ChequeredMaterial:
    """Material with chessboard pattern"""

    def __init__(self,color1 = Color.from_hex("#ffffff"),color2 = Color.from_hex("#000000"),
    ambient = 0.05, diffuse = 1.0, specular = 1.0, reflection=0.5):
        self.color1 = color1
        self.color2 = color2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self,pos):
        if int((pos.x + 5.0)*3.0)%2 == int(pos.z * 3.0) % 2:
            return self.color1
        else:
            return self.color2