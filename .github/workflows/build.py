import os
import sys
import ntpath
import glob

math_jax_script = '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>'

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def main(file, directory):
    print("printing file and directory", file, directory)
#     I probabaly dont need to check if hte file ends with md since the github action only passes md files but thats fine
    if (file.endswith(".md") and not file.startswith('.github') and ntpath.basename(file) != "index.md"):

        with open(file) as f:
            first_line = f.readline()

        if first_line != math_jax_script:
            line_prepender(file, math_jax_script)

        file_path = os.path.normpath(file)

        file_location_array = file_path.split(os.sep)

        print('file_path', file_path)

        print('file_location_array', file_location_array)


        with open(os.path.split(file_path)[0] + "/index.md") as index:

            print(f"# {file_location_array[-2]}")
#             index.write(f"# {file_location_array[-2]}")

            files = [fn for fn in glob(f"{file_path.split()[0]}*.md")
                     if not os.path.basename(fn).startswith('index')]

            print("files", files)

            for fn in files:
                print(f"[{file_location_array[-1]}]({file_location_array[-1]})\n\n")
#                 f.write(f"[{file_location_array[-1]}]({file_location_array[-1]})\n\n")








#         new_name = os.path.split(file)[1].replace(" ", "-")
#         folder = new_name.split("-")[0].capitalize()

        if not file.startswith("markdown"):
#             folder = file.split("-")[0].capitalize()
#             os.makedirs(f"_notes/{folder}", exist_ok=True)
            os.rename(file, f"markdown/Other/{os.path.split(file)[1]}")
        else:
            # build the index files for sub folders
            # use index.md it will be muhc better
            print('is in notes')


#         if(file == f"markdown/{folder}/{new_name}"):
#             print(f"file already formatted, only edit required \n")
#         else:
#             os.rename(directory + os.sep + file, f"markdown/{folder}/{new_name}")
#             line_prepender(f"markdown/{folder}/{new_name}", '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>')
#
#         file = os.path.split(file)
#
        subject_sub = glob.glob("markdown/*/")

        print("subjects", list(subject_sub))
#
        f = open(directory + "/index.md", 'w')
        f.write("# File Sharing")

        f.write("\n\n")
#
        for subject in list(subject_sub):

            file_sub = glob.glob(f"{subject}/*/")

            if len(list(file_sub)) > 0:

                f.write(f"## { os.path.normpath(subject).split(os.sep)[-1] } \n")

                for sub_file in list(file_sub):

#                     print("SUB FILE!!!", sub_file)

                    my_path = os.path.normpath(sub_file)

                    path_list = my_path.split(os.sep)

                    print(f">[{path_list[-1]}/]({sub_file}/)\n>\n")

                    f.write(f">[{path_list[-1]}]({sub_file + path_list[-1]})\n>\n")

                f.write("\n")

        f.close()


#             subfiles = next(os.walk(directory + "/" + subdirs[i]))[2]
#
#             if len(subfiles) > 0:
#                path = os.path.normpath(subdirs[i])
#                f.write(f"## {path.split(os.sep)[-1]} \n")
#
#             for j in range(len(subfiles)):
#                 f.write(f">[{os.path.splitext(ntpath.basename(subfiles[j]))[0]}]({subdirs[i] + os.path.splitext(ntpath.basename(subfiles[j]))[0]})\n>\n")
#
#             f.write("\n")
#
#         f.close()
#

if __name__ == "__main__":

    print('system arguments', sys.argv)
    all_files = sys.argv[1].split(",")

    for file in all_files:
        print("print file", file)
        main(file, sys.argv[-1])

