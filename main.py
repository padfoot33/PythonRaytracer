#!/usr/bin/env python
"""A Python Raytracer by Param Joshi, 2020"""

from image import Image
from color import Color
from Vector import Vector
from point import Point
from sphere import Sphere
from engine import RenderEngine
from scene import Scene

def main():
    WIDTH = 320
    HEIGHT = 200
    
    camera = Vector(0,0,-1)
    objects = [
        Sphere(Point(0, -0.25, 0), 0.1, Color.from_hex("#cc0000")),
        Sphere(Point(0, 0, 0), 0.1, Color.from_hex("#edd400")),
        Sphere(Point(0, +0.25, 0), 0.1, Color.from_hex("#4e9a06")),
    ]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()