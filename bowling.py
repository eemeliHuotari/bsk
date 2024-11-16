from bowling_error import BowlingError
from frame import Frame


class BowlingGame:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) >= 10:
            raise BowlingError("Cannot add more than 10 frames to a game.")
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i < 0 or i >= len(self.frames):
            raise BowlingError("Frame index out of range.")
        return self.frames[i]
    
    def calculate_score(self) -> int:
        return sum(frame.first_throw + frame.second_throw for frame in self.frames)