import os
import sys
import getopt
import re

def main(file, directory):
    print("the file is", file)
    if(file.endswith(".md") and not file.startswith('.github')):
        x = re.search("(\/(?!.*\/)).*$", file)
        print(x.string)
        print("SUCCESS!!!!")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
