import os

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")
