from toki import translate
import unittest
import sys
sys.path.append("/home/codio/workspace/student_code")


class TestTranslator(unittest.TestCase):
    def test_translate(self):
        answers = {
            "Someone is good.": "jan li pona.",
            "They are sleeping.": "oni li lape.",
            "You are good.": "sina li pona.",
            "Love is good.": "olin li pona.",
            "My food is bad.": "mi moku li ike.",
            "I am your friend.": "mi jan sina pona.",
        }
        for key in answers:
            print(f'Expected: {answers[key]}')
            print(f'Got:      {translate(key)}')
            self.assertTrue(translate(key) == answers[key])
            print()


if __name__ == '__main__':
    unittest.main()
