import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_add_and_get_frames(self):
        game = BowlingGame()
        for i in range(10):
            game.add_frame(Frame(i, i + 1))
        for i in range(10):
            frame = game.get_frame_at(i)
            self.assertEqual(frame.first_throw, i)
            self.assertEqual(frame.second_throw, i + 1)
        with self.assertRaises(BowlingError):
            game.add_frame(Frame(0, 0))
        with self.assertRaises(BowlingError):
            game.get_frame_at(10)
            
    def test_calculate_score(self):
            game = BowlingGame()
            game.add_frame(Frame(1, 5))
            game.add_frame(Frame(3, 6))
            game.add_frame(Frame(7, 2))
            game.add_frame(Frame(3, 6))
            game.add_frame(Frame(4, 4))
            game.add_frame(Frame(5, 3))
            game.add_frame(Frame(3, 3))
            game.add_frame(Frame(4, 5))
            game.add_frame(Frame(8, 1))
            game.add_frame(Frame(2, 6))
            expected_score = 6 + 9 + 9 + 9 + 8 + 8 + 6 + 9 + 9 + 8
            self.assertEqual(game.calculate_score(), expected_score)