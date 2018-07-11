"""
An Xml Task

"""

import xml.etree.ElementTree as xml
#test_root = xml.fromstring("<a><b>test</b></a>")
data = xml.parse("task5.xml")
root = data.getroot()

def get_view(root, space):
    result = ""
    for i in root:
        attr = "" if i.attrib == {} else i.attrib
        s = "" if space == 0 else " "*space
        result+="{}{}{} {}\n".format(s, i.tag, attr, i.text)
        if len(i)>0:
                result+=get_view(i,space+1)
    return result


def get_value_by_tag(tag,root):
    values = []
    for i in root:
        if i.tag == tag:
            values.append(i.text)
        if len(i)>0:
            result = get_value_by_tag(tag,i)
            if len(result) > 0:
                values+=result
    return values


def count_tags_by_attrib(attrib,root):
    total = 0
    for i in root:
        if attrib in i.attrib:
            total+=1
        if len(i)>0:
            total += count_tags_by_attrib(attrib,i)
    return total


#print(get_view(root,0))
#print(get_value_by_tag("pc_item", root))
#print(count_tags_by_attrib("name",root))
#print(get_view(test_root,0))
