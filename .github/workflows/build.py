import os
import sys
import getopt
import re

def main(file, directory):
    print("the file is", file)
    print('the directory is ', directory)
    print(re.search("(\/(?!.*\/)).*$", file).string)
    if(file.endswith(".md") and not file.startswith('.github')):
        x = re.search("(\/(?!.*\/)).*$", file)
        print(x)
        print("SUCCESS!!!!")


if __name__ == "__main__":
    print(sys.argv[0])
    main(sys.argv[1], sys.argv[2])
