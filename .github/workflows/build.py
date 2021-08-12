import os
import sys
import getopt
import ntpath

def main(file, directory):

    if(file.endswith(".md") and not file.startswith('.github') and ntpath.basename(file) != "index.md"):
#         print("SUCCESS!!")
        print(directory+"/"+file)
        print(directory+"/markdown/"+ntpath.basename(file))
#         print(os.path.dirname(os.path.realpath(file)))
        os.rename(directory+"/"+file, directory+"/markdown/"+ntpath.basename(file))
        os.lstdir(directory+"/markdown/)


if __name__ == "__main__":
    print(sys.argv[0])
    main(sys.argv[1], sys.argv[2])
