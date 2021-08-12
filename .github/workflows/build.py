import os
import sys
import getopt
import ntpath

def main(file, directory):

    if(file.endswith(".md") and not file.startswith('.github') and ntpath.basename(file) != "index.md"):
#         print("SUCCESS!!")
        os.rename(directory+file, directory+"/markdown/"+ntpath.basename(file))


if __name__ == "__main__":
    print(sys.argv[0])
    main(sys.argv[1], sys.argv[2])
