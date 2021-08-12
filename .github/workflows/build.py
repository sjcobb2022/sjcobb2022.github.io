import os
import sys
import getopt
import re

def main(file, directory):
    print("the file is", file)
    print(os.getcwd())
#     os.rename(file, files+1)
    if(file.endswith(".md") and not file.startswith('.github')):
        x = re.search("(\/(?!.*\/)).*$", file)
        os.rename(file, directory+x.string)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
