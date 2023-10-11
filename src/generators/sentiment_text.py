import os
import random
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import paths
import utils

if __name__ == "__main__":
    positive_words = [
        "great",
        "excellent",
        "good",
        "fantastic",
        "nice",
        "happy",
        "superb",
        "awesome",
        "pleasing",
        "delightful",
        "cherubic",
        "spectacular",
        "wonderful",
        "pleasant",
    ]
    negative_words = [
        "terrible",
        "horrible",
        "awful",
        "atrocious",
        "bad",
        "horrendous",
        "heinous",
        "distressing",
        "baleful",
        "nauseating",
        "terrifying",
        "stupid",
        "dumb",
        "appauling",
        "stupefying",
    ]

    pos_dir = os.path.join(paths.TEXT, "positive")
    neg_dir = os.path.join(paths.TEXT, "negative")

    utils.mkdirp(pos_dir)
    utils.mkdirp(neg_dir)

    for i in range(0, 1000):
        text = " ".join((random.choice(positive_words) for _ in range(0, 5)))
        fp = os.path.join(paths.TEXT, "positive", f"{i}.txt")
        with open(fp, "w") as f:
            f.write(text)

    for i in range(0, 1000):
        text = " ".join((random.choice(negative_words) for _ in range(0, 5)))
        fp = os.path.join(paths.TEXT, "negative", f"{i}.txt")
        with open(fp, "w") as f:
            f.write(text)
