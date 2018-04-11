# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.4.11
# 单元测试：测试类
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    # 先运行setUp，再运行test_开头的函数
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    # 测试单个响应是否存储成功
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    # 测试3个响应是否存储成功
    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
