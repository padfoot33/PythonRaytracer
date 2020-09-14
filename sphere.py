from math import sqrt
class Sphere:
    """Sphere shape implimentation, has center, radius, material"""

    def __init__(self,center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self,ray):
        """Checks if Ray intersects with sphere, returns distance to intersection or non if no intersection"""
        sphere_to_ray = ray.origin - self.center
        #a = 1
        b = 2*ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius*self.radius
        discriminent = b*b - 4*c

        if discriminent>=0:
            dist = (-b -sqrt(discriminent))/2
            if dist>0:
                return dist
        return None