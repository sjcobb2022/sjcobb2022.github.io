import os
import sys
import ntpath


def main(file, directory):
    print(file, directory)
    if (file.endswith(".md") and not file.startswith('.github') and ntpath.basename(file) != "index.md"):
        os.rename(directory + "/" + file, directory + "/markdown/" + ntpath.basename(file))
        print(directory + "/" + file, directory + "/markdown/" + ntpath.basename(file))

        dirs = os.listdir(os.cwd())

        for file in dirs:
           print(file)

        f = open(directory + "/index.md", 'a')
        f.write(f"<br>"
                f"\n"
                f"\n"
                f"\n"
                f">[{ntpath.basename(file)}]({'/markdown/' + os.path.splitext(ntpath.basename(file))[0]})"
                f"\n"
                f"\n"
                f"<br>"
                f"\n"
                f"")


if __name__ == "__main__":
    print(sys.argv[0])
    main(sys.argv[1], sys.argv[2])
