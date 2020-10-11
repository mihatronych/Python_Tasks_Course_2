# Работа с файлами

#r (read) - открыть для чтения (по умолчанию)
# w (write) - открыть для записи, запись ведется в конец
# b (binary) - открыть в бинарном режиме
# t (text) - открыть в текстовом режиме (по умолчанию)
# r* - открыть для чтения и записи
# w* - открыть для чтения и записи, содержимое файла стирается
# a (append) - дозапись
# Чтение из файла
f = open("file.txt", "r")

for line in f:
    line = line.rstrip()
    print(repr(line))

x = f.read()

#x = f.readline().rstrip() #считать одну строку

#x = f.read()  #считать все

#x = x.splitlines()  #сплитить по строкам
# print(repr(x))

#x = f.read(5)  #считатать 5 символов
#print(x)
#y = f.read()  #считать все
#print(y)

f.close()


# Запись в файл
f = open("some.txt", "w")

f.write("Hello\n")
f.write("World!")
lines = ["Line 1", "Line 2", "Line 3"]
contents = "\n".join(lines)
f.write(contents)

f.close()

# Дозапись в файл
f = open("text_append.txt", "a")
f.write("Hello\n")

f.close()

f = open("text_append.txt", "a")
f.write("World!\n")

f.close()

with open("file.txt") as f, open("text_copy.txt", "w") as w:  #Инерпретатор гарантированно закроет файл, поэтому это правильнее
    for line in f:
        w.write(line)

# Всякое с os.path()
import os
import os.path

print(os.getcwd()) # путь до директории
print(os.listdir(".idea"))  # список файлов в директории

print(os.path.exists("file.txt")) # есть ли такой файл
print(os.path.exists("random.py"))
print(os.path.exists("tests"))

print(os.path.abspath("file.txt")) # абсолютный путь до файла

#os.chdir(".idea") изменить директорию файла на указанную

import shutil # С помощью него всякое можно копировать

shutil.copy("newfile.txt", "newfile2.txt")

for current_dir, dirs, files in os.walk("."): # рекурсивный вывод всех папок, подпапок файлов и т.д.
    print(current_dir, dirs, files)
