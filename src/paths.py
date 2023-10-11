import os

fpath = os.path.dirname(__file__)
datapath = os.path.join(fpath, "..", "data")

IMAGES = os.path.join(datapath, "./shapes/")
TEXT = os.path.join(datapath, "./sentiment_text/")
RANDOM_TABULAR_DIR = os.path.join(datapath, "./random_tabular/")
RANDOM_TABULAR_FILE = os.path.join(RANDOM_TABULAR_DIR, "./data.json")
