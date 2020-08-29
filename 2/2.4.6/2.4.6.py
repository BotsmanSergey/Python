import os
os.chdir(r"C:\\Learning\Python\2\2.4.6")
with open("writefile.txt", "w") as writefile:
    for current_dir, dirs, files in os.walk("main"):
        for py in files:
            if '.py' in py:
                writefile.write(current_dir + "\n")
                break