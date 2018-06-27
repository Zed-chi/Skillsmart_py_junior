"""
python -m unittest test_task5.py
"""

import unittest
from task5 import count_tags_by_attrib,get_value_by_tag,get_view


class TaskTests(unittest.TestCase):
    import xml.etree.ElementTree as xml
    root = xml.fromstring("<a><b>test</b></a>")

    def test_view(self):
        get_view(self.root, 0)
        assert get_view(self.root, 0) == "b test\n"

    def test_values_by_tags(self):
        assert get_value_by_tag("b", self.root) == ['test']

    def test_tags_by_attrib(self):
        assert count_tags_by_attrib("name",self.root) == 0


if __name__ == "__main__":
    unittest.main()