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
        total_score = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            frame_score = frame.first_throw + frame.second_throw

            if frame.is_spare():
                if i + 1 < len(self.frames):
                    frame_score += self.frames[i + 1].first_throw

            total_score += frame_score

        return total_score