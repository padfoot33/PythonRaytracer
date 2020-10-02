class Scene:
    """Scene has all the information needed for the RayTracing Engine"""
    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
        self.lights = lights