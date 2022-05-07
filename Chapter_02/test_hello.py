# unittestモジュールを読み込んで利用

import unittest

class TestFunc(unittest.TestCase):
    def test_func(self):
        from hello import func
        self.assertIsNone(func("こんにちわ"))