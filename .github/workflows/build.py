import os
import sys
import ntpath

def main(file, directory):
    print(file, directory)
    if (file.endswith(".md") and not file.startswith('.github') and ntpath.basename(file) != "index.md"):
        os.rename(directory + "/" + file, directory + "/markdown/" + ntpath.basename(file))
        print(directory + "/" + file, directory + "/markdown/" + ntpath.basename(file))


        print([x[0] for x in os.walk(directory+"./markdown/")])

        f = open(directory + "/index.md", 'a')
        f.write(f">[{os.path.splitext(ntpath.basename(file))[0]}]({'/markdown/' + os.path.splitext(ntpath.basename(file))[0]})")
        f.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])