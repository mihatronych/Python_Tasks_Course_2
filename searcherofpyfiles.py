import os

ar = []
with open("newfile2.txt", "w") as w:
    for current_dir, dirs, files in os.walk("main"):
        for f in files:
            if f[-3:] == ".py":
                print(current_dir)
                ar.append(current_dir)
                break
    ar.sort()
    w.write("\n".join(ar))

print(ar)
