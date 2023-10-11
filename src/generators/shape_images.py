from PIL import Image, ImageDraw

import os
import random
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import paths
import utils


def draw_circle(img, x, y, r):
    draw = ImageDraw.Draw(img)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0,0))


def draw_rect(img, x, y, w, h):
    draw = ImageDraw.Draw(img)
    draw.rectangle([(x, y), (x+w, y+h)], fill ="#ffff33", outline ="red")


if __name__ == "__main__":
    circles_dir = os.path.join(paths.IMAGES, "circles")
    rects_dir = os.path.join(paths.IMAGES, "rectangles")

    utils.mkdirp(circles_dir)
    utils.mkdirp(rects_dir)

    for i in range(0, 200):
        x = random.randint(150, 350)
        y = random.randint(150, 350)
        r = random.randint(10, 100)

        img = Image.new('RGB', (500, 500))
        draw_circle(img, x, y, r)
        img.save(os.path.join(circles_dir, f"circle_{i}.png"))

    print("Saved circles")

    for i in range(0, 200):
        x = random.randint(0, 350)
        y = random.randint(0, 350)
        w = random.randint(50, 150)
        h = random.randint(50, 150)

        img = Image.new('RGB', (500, 500))
        draw_rect(img, x, y, w, h)
        img.save(os.path.join(rects_dir, f"rectangle_{i}.png"))

    print("Saved rectangles")
