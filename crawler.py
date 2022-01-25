import glob
import sys

path = sys.argv[2]

for filename in glob.iglob(path + '/**', recursive=True):
    print(filename)
