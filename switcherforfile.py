with open("dataset_24465_4(1).txt", "r") as o, open("newfile.txt", "w") as w:
    f = w.write("".join(o.readlines()[::-1]))
