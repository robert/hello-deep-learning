import os

def mkdirp(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
