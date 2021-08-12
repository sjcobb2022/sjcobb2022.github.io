import os
import sys
import getopt
import re

def main(file, directory):
    print("the file is", file)
    print(os.getcwd())
    if(file.endswith(".jpg") and not file.startswith('.github')):
        x = re.search("(\/(?!.*\/)).*$", file)
        os.rename(file, directory)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
