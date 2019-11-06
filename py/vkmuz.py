import os
import sys
from os import listdir
from os.path import isfile, join

govnostr = " (music7s.com)"

if __name__ == '__main__':
    files = [f for f in listdir(sys.path[0]) if isfile(join(sys.path[0], f))]
    for f in files:
        try:
            fixedfilename = f.replace(govnostr, '')
            os.rename(f, fixedfilename)
        except Exception as e:
            print(e)


def main():
    sys.argv.pop(0)
    print(sys.argv)
    if len(sys.argv) > 0:
        for path in sys.argv:
            dir = os.path.split(path)[0]
            filename = os.path.split(path)[1]
            fixedfilename = filename.replace(govnostr, '')
            #os.system(path)
            print("REN \"" + path + "\" \"" + os.path.join(dir, fixedfilename) + "\"")
            os.system("REN \"" + path + "\" \"" + os.path.join(dir, fixedfilename) + "\"")
            #os.rename(path, os.path.join(dir, fixedfilename))

    else:
        print("err")
