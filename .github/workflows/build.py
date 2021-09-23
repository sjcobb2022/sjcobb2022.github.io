import os
import sys
import ntpath
import glob

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def main(file, directory):
    print(file, directory)
#     I probabaly dont need to check if hte file ends with md since the github action only passes md files but thats fine
    if (file.endswith(".md") and not file.startswith('.github') and ntpath.basename(file) != "index.md"):

        new_name = os.path.split(file)[1].replace(" ", "-")
        folder = new_name.split("-")[0].capitalize()

        os.makedirs(f"markdown/{folder}", exist_ok=True)

        if(file == f"markdown/{folder}/{new_name}"):
            print(f"file already formatted, only edit required \n")
        else:
            os.rename(directory + os.sep + file, f"markdown/{folder}/{new_name}")
            line_prepender(f"markdown/{folder}/{new_name}", '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>')

        file = os.path.split(file)

        subdirs = glob.glob("markdown/*/")


        f = open(directory + "/index.md", 'w')
        f.write("# File Sharing")
        f.write("\n\n")

        for i in range(len(subdirs)):
            subfiles = next(os.walk(directory + "/" + subdirs[i]))[2]

            if len(subfiles) > 0:
               path = os.path.normpath(subdirs[i])
               f.write(f"## {path.split(os.sep)[-1]} \n")

            for j in range(len(subfiles)):
                f.write(f">[{os.path.splitext(ntpath.basename(subfiles[j]))[0]}]({subdirs[i] + os.path.splitext(ntpath.basename(subfiles[j]))[0]})\n>\n")

            f.write("\n")

        f.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])