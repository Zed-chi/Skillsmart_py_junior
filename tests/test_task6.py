"""
python -m unittest test_tas6.py
"""

import unittest
from task6 import *


class TaskTests(unittest.TestCase):
    import xml.etree.ElementTree as xml
    s = "<data><a><aa>1</aa><aa>2</aa><aa>3</aa><aa>4</aa><aa>5</aa></a><b><bb>1</bb><bb>1</bb><bb>1</bb></b><d><aa>0</aa></d><e></e></data>"
    root = xml.fromstring(s)

    def test_tag_list(self):
        print("debug should {}".format(len(get_xml_by_tag(self.root,"bb"))))
        assert len(get_xml_by_tag(self.root,"bb")) == 3

    def test_find_parent(self):
        elem = get_xml_by_tag(self.root, "aa")
        assert find_parent(self.root,elem[5]) == self.root.find("d")

    def test_remove_by_tag(self):
        assert len(remove_node_by_tag("a",self.root)) == 3


if __name__ == "__main__":
    unittest.main()


"""
структура теструемого xml

<data>
    <a>
        <aa>1</aa>
        <aa>2</aa>
        <aa>3</aa>
        <aa>4</aa>
        <aa>5</aa>
    </a>
    <b>
        <bb>1</bb>
        <bb>1</bb>
        <bb>1</bb>
    </b>
    <d>
        <aa>0</aa>
    </d>
    <e></e>
</data>

"""
