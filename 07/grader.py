from movies import frequent_words
import unittest
import sys
sys.path.append("/home/codio/workspace/student_code")


def load_script(fname):
    script = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            script.append(clean_line(line, ".,!?:\"'()=-@#$%^&*<>\\/"))
    return script


def clean_line(line, bad_characters):
    for bchar in bad_characters:
        line = line.replace(bchar, "")
    return line


class TestTranslator(unittest.TestCase):
    def test_translate(self):
        answers = {
            "scripts/bee.txt": 517,
            "scripts/field_dreams.txt": 934,
            "scripts/inception.txt": 1234,
            "scripts/scott_pilgrim.txt": 661,
            "scripts/sense_sensibility.txt": 767,
            "scripts/Shrek.txt": 467
        }
        for key in answers:
            the_count = frequent_words(load_script(key))
            print(f'Expected: [***, {answers[key]}]')
            print(f'Got:      {the_count}')
            self.assertTrue(the_count == ["the", answers[key]])
            print()


if __name__ == '__main__':
    unittest.main()
