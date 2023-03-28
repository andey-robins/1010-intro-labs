from movies import frequent_words
import unittest
import sys
sys.path.append("/home/codio/workspace/student_code")


def load_script(fname):
    script = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            script.append(clean_line(line, ".,!?:\"'()=-@#$%^&*<>\\/").lower())
    return script


def clean_line(line, bad_characters):
    for bchar in bad_characters:
        line = line.replace(bchar, "")
    return line


class TestTranslator(unittest.TestCase):
    def test_translate(self):
        answers = {
            "scripts/bee.txt": [[610, 'barry'], [246, 'vanessa'], [153, 'adam'], [129, 'bee'], [101, 'out']],
            "scripts/field_dreams.txt": [[809, 'ray'], [276, 'annie'], [271, 'mann'], [195, 'continued'], [115, 'karin']],
            "scripts/inception.txt": [[727, 'cobb'], [253, 'ariadne'], [225, 'arthur'], [165, 'saito'], [162, 'fischer']],
            "scripts/scott_pilgrim.txt": [[1111, 'scott'], [435, 'ramona'], [314, 'continued'], [261, 'knives'], [184, 'wallace']],
            "scripts/sense_sensibility.txt": [[550, 'elinor'], [489, 'marianne'], [428, 'mrs'], [299, 'dashwood'], [197, 'not']],
            "scripts/Shrek.txt": [[417, 'shrek'], [316, 'donkey'], [207, 'fiona'], [114, 'no'], [106, 'me']]
        }
        for key in answers:
            res = frequent_words(load_script(key))
            print(f'Expected: {answers[key]}')
            print(f'Got:      {res}')
            self.assertTrue(res == answers[key])
            print()


if __name__ == '__main__':
    unittest.main()
