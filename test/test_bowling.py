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
            
