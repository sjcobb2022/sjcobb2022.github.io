import os
import sys
import getopt
import re

def main(file, directory):
    print("the file is", file)
    if(file.endswith(".md") and not file.startswith('.github')):
        print("SUCCESS!!!!")
        x = re.search("(\/(?!.*\/)).*$", file)
        os.rename(file, directory+x.string)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
