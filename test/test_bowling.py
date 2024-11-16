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
            
    def test_calculate_score_with_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 9))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        expected_score = 13 + 9 + 9
        self.assertEqual(game.calculate_score(), expected_score)

    def test_spare_in_last_frame(self):
        game = BowlingGame()
        for _ in range(9):
            game.add_frame(Frame(3, 6))
        game.add_frame(Frame(5, 5))
        expected_score = (9 * 9) + 10
        self.assertEqual(game.calculate_score(), expected_score)
        
    def test_calculate_score_with_strike(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        expected_score = 19 + 9 + 9
        self.assertEqual(game.calculate_score(), expected_score)
        
    def test_consecutive_strikes(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 2))
        expected_score = 27 + 19 + 9
        self.assertEqual(game.calculate_score(), expected_score)

    def test_strike_in_last_frame(self):
        game = BowlingGame()
        for _ in range(9):
            game.add_frame(Frame(3, 6)) 
        game.add_frame(Frame(10, 0))
        expected_score = (9 * 9) + 10
        self.assertEqual(game.calculate_score(), expected_score)
        
    def test_strike_followed_by_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(4, 6))
        game.add_frame(Frame(7, 2))
        expected_score = 20 + 17 + 9
        self.assertEqual(game.calculate_score(), expected_score)

    def test_strike_spare_and_normal_frame(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(6, 4))
        game.add_frame(Frame(3, 2))
        expected_score = 20 + 13 + 5
        self.assertEqual(game.calculate_score(), expected_score)
        
    def test_multiple_strikes(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 2))
        expected_score = 27 + 19 + 9
        self.assertEqual(game.calculate_score(), expected_score)

    def test_multiple_strikes_with_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 3))
        game.add_frame(Frame(8, 1))
        expected_score = 27 + 20 + 18 + 9
        self.assertEqual(game.calculate_score(), expected_score)
        
    def test_multiple_spares(self):
        game = BowlingGame()
        game.add_frame(Frame(8, 2))
        game.add_frame(Frame(5, 5))
        game.add_frame(Frame(7, 2))
        expected_score = 15 + 17 + 9
        self.assertEqual(game.calculate_score(), expected_score)

    def test_spare_followed_by_strike(self):
        game = BowlingGame()
        game.add_frame(Frame(8, 2))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 2))
        expected_score = 20 + 19 + 9
        self.assertEqual(game.calculate_score(), expected_score)
        
    def test_spare_as_last_frame(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 2))
        game.set_first_bonus_throw(7)
        expected_score = 56 + 17
        self.assertEqual(game.calculate_score(), expected_score)

    def test_no_bonus_for_non_spare_last_frame(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(9, 1))
        game.set_first_bonus_throw(7)
        expected_score = (1 + 5) + (3 + 6) + (7 + 2) + (3 + 6) + (4 + 4) + (5 + 3) + (3 + 3) + (4 + 5) + (9 + 1)
        self.assertEqual(game.calculate_score(), expected_score)