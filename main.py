#!/usr/bin/env python
"""A Python Raytracer by Param Joshi, 2020"""
import argparse
import importlib
import os

from scene import Scene
from engine import RenderEngine

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene",help="Path to Scene File(without .py extention")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)

    scene = Scene(mod.CAMERA,mod.OBJECTS,mod.LIGHTS,mod.WIDTH,mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))

    with open(mod.RENDERED_IMG, "w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()