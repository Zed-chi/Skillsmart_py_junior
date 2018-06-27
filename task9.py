"""
Image handling with Pillow Library

"""

def convert(ext_from, ext_to,path):
    from PIL import Image
    import os
##    получить список файлов
    files = os.listdir(path)
##    определить файлы с нужным расширением
    files_to_convert = list()
    for i in files:
        if os.path.splitext(i)[1] == ext_from:
            files_to_convert.append(i)
##    открыть/конвертировать
    for i in files_to_convert:
        im = Image.open(path+"/"+i)
        name =path + "/" + os.path.splitext(i)[0] + ext_to
        im.save(name)


def type_text_and_convert(ext_from, ext_to,path):
    from PIL import Image,ImageDraw
    import os
##    получить список файлов
    files = os.listdir(path)
##    определить файлы с нужным расширением
    files_to_convert = list()
    for i in files:
        if os.path.splitext(i)[1] == ext_from:
            files_to_convert.append(i)
##    открыть/конвертировать
    for i in files_to_convert:
        im = Image.open(path+"/"+i)
        im = im.convert('RGBA')
        center = [int(x/2) for x in im.size]
        #создаем прямоугольник
        sq = Image.new("RGBA", (100,100),(0,0,0,0))
        draw = ImageDraw.Draw(sq)
        #добавляем текст
        draw.multiline_text((10,10), 'Hello\nworld', fill="blue")
        im.paste(sq,(center[0]-50,center[1]-50))
        name = path + "/1" + os.path.splitext(i)[0] + ext_to
        im.save(name)

##convert(".jpeg",".png","task9")
#type_text_and_convert(".jpeg",".png","task9")

