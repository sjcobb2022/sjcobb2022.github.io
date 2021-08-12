import os
import sys
import getopt


def main(file):
    print("the file is", file)
    if(file.endswith(".yml")):
        print('it ends with yml')

if __name__ == "__main__":
    main(sys.argv[1])
