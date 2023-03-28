from genes import count_vulnerable_genomes
import unittest
import sys
sys.path.append("/home/codio/workspace/student_code")


class TestTranslator(unittest.TestCase):
    def test_translate(self):
        answers = {
            "genes_test.txt": 1,
            "genes_small.txt": 33,
            "genes.txt": 389
        }
        for key in answers:
            vulnerable = count_vulnerable_genomes(key)
            print(f'Expected: {answers[key]}')
            print(f'Got:      {vulnerable}')
            self.assertTrue(vulnerable == answers[key])
            print()


if __name__ == '__main__':
    unittest.main()
