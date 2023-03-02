from game import player_chose_rock, player_chose_paper, player_chose_scissors, find_winner
import unittest
import sys
sys.path.append("/home/codio/workspace/student_code/")


class TestPlayerChoseRock(unittest.TestCase):
    def test_draw(self):
        self.assertTrue(player_chose_rock("r") == "draw")

    def test_player(self):
        self.assertTrue(player_chose_rock("s") == "player")

    def test_computer(self):
        self.assertTrue(player_chose_rock("p") == "computer")


class TestPlayerChosePaper(unittest.TestCase):
    def test_draw(self):
        self.assertTrue(player_chose_paper("p") == "draw")

    def test_player(self):
        self.assertTrue(player_chose_paper("r") == "player")

    def test_computer(self):
        self.assertTrue(player_chose_paper("s") == "computer")


class TestPlayerChoseRock(unittest.TestCase):
    def test_draw(self):
        self.assertTrue(player_chose_scissors("s") == "draw")

    def test_player(self):
        self.assertTrue(player_chose_scissors("p") == "player")

    def test_computer(self):
        self.assertTrue(player_chose_scissors("r") == "computer")


class TestFindWinner(unittest.TestCase):
    def test_draw(self):
        self.assertTrue(find_winner("p", "p") == "draw")
        self.assertTrue(find_winner("s", "s") == "draw")
        self.assertTrue(find_winner("r", "r") == "draw")

    def test_player(self):
        self.assertTrue(find_winner("p", "r") == "player")
        self.assertTrue(find_winner("r", "s") == "player")
        self.assertTrue(find_winner("s", "p") == "player")

    def test_computer(self):
        self.assertTrue(find_winner("r", "p") == "computer")
        self.assertTrue(find_winner("s", "r") == "computer")
        self.assertTrue(find_winner("p", "s") == "computer")


if __name__ == '__main__':
    unittest.main()
