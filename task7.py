'''
path funcs
os and os.path module

'''

import os.path

def get_files_and_dirs(path):
    file_arr = []
    dir_arr = []
    for root,dirs,files in os.walk(path):
        file_arr+=files
        dir_arr+=(dirs)
    return [file_arr,dir_arr]


def del_dir(path):
    if not os.path.isdir(path):
        raise NameError("Папка не существует")
        return None
    a = get_files_and_dirs(path)
    files = a[0]
    dirs = a[1]
    if len(dirs)==0:
        if len(files)>0:
            for i in files:
                os.remove(path+'/'+i)
        os.rmdir(path)
    else:
        raise NameError("Папка содержит подкаталог")


#del_dir("rem")
#get_files_and_dirs("C:/")
