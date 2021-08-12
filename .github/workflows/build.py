import os
import sys
import getopt
import ntpath

def main(file, directory):

    if(file.endswith(".md") and not file.startswith('.github')):
        print("SUCCESS!!")
        print(ntpath.basename(file))
        print(os.getcwd()+"/"+ntpath.basename(file))


if __name__ == "__main__":
    print(sys.argv[0])
    main(sys.argv[1], sys.argv[2])
