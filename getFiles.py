import glob
with open('getFiles.txt',"w") as f:
    f.write('Python Files\n\n')
    for file in glob.glob("*.py"):
        f.write(f"{file}\n")
    f.write("\nTXT Files\n\n")
    for file in glob.glob("*.txt"):
        f.write(f"{file}\n")