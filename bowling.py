from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
        self.max_frames = 10
    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) < self.max_frames:
            self.frames.append(frame)
        else:
            raise BowlingError

    def get_frame_at(self, i: int) -> Frame:
        if 0 <= i < len(self.frames):
            return self.frames[i]
        else:
            raise BowlingError

    def calculate_score(self) -> int:
        pass

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
