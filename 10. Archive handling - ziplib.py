"""
Archive handling task
ziplib module

"""


def add_files_to_arc(archive, ext):
    from zipfile import ZipFile
    import os
##    проверить существование файла
    if not os.path.exists(archive):
        dir = os.path.dirname(archive)
        try:
            os.makedirs(dir)
        except:
            pass
        with open(archive, "w") as f:
            pass
##    получить список файлов в каталоге
    files = os.listdir(".")
##    определить файлы с нужным расш.
    files_to_add = [i for i in files if os.path.splitext(i)[1] == ext]
##    добавить их в архив
    with ZipFile(archive, "w") as zip:
        for i in files_to_add:
            zip.write(i)


add_files_to_arc("task10_1/test.zip", ".txt")
