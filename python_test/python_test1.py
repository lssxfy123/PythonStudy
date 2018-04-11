# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 单元测试：测试函数
import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    # 测试函数需要以test_开头
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
