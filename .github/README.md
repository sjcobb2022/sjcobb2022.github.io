# >[sjcobb2022.github.io](sjcobb2022.github.io)


## Formatting

All notes have been formatted in markdown with jekyll rendering. Default git theme used because it's a lot nicer for notes.

### Mathjax

Every new file is auto-formatted with MathJax, and therefore LaTeX is default.

For inline LaTeX, simply write equation in a continuous line $$Like This$$. Otherwise, just make a new line before a new equation if you want it centered.


## Naming conventions

All files should be named in the same convention to prevent bugs.

```subject-?info-date[dd-mm-yyyy]```


> **Example**: ```Business-10-9-2021``` or ```Physics-Kognity-06-11-2020```

additional info is optional, but it can be used to specify the type of work



> **WARNING**: No spaces should be used in file names as it messes with my git action.


<br/>

### Uploading

The build python script should take care of any new markdown files. Files can be uploaded to any directory (other than ```.github```), and the file will be formatted and placed in the correct folder.

If the file already exists, an error is thrown