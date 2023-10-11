import json
import os
import random
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import paths
import utils


if __name__ == "__main__":
    data = []

    for i in range(0, 10000):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(0, 100)
        d = random.randint(0, 100)
        e = random.randint(0, 100)
        f = random.randint(0, 100)

        y = 0
        if (a < 5 and b > 90):
            y = 1
        elif (b > 50 and (c > 10 and c < 30)):
            y = 2
        elif (c < 3 or c > 97):
            y = 3
        elif (d > 60 and d < 90):
            y = 4
        elif (e > 80 and e < 90):
            y = 5
        elif (f > 10 and f < 25):
            y = 6

        data.append({
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'e': e,
            'f': f,
            'y': y,
        })

    utils.mkdirp(paths.RANDOM_TABULAR_DIR)

    fpath = os.path.join(paths.RANDOM_TABULAR_FILE, "data.json")
    with open(fpath, "w") as f:
        json.dump(data, f)
