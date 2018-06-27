"""
An Xml Task
xml.etree.ElementTree module
"""

import xml.etree.ElementTree as xml

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


def remove_node_by_tag(tag,root):
    copy = root
    def rem(tag,root):
        for node in root:
            if len(node)>0:
                rem(tag,node)
        finded = root.findall(tag)
        for sub_node in finded:
            root.remove(sub_node)
    rem(tag,copy)
    return copy


def get_xml_by_tag(root, tag):
    res = []
    res += root.findall(tag)
    for i in root:
        if len(i)>0:
            res += get_xml_by_tag(i, tag)
    return res


def find_parent(root,elem):
    if elem in root:
        return root
    for i in root:
        parent = find_parent(i,elem)
        if parent == None:
            continue
        else:
            return parent
    return None


s = "<data><a><aa>1</aa><aa>2</aa><aa>3</aa><aa>4</aa><aa>5</aa></a><b><bb>1</bb><bb>1</bb><bb>1</bb></b><d><aa>0</aa></d><e></e></data>"
test = xml.fromstring(s)
#print(get_view(test, 0))
