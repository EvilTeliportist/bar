import time, math, sys

class ProgressBar:
    def __init__(self, min, max, unfilled = "-", filled = '■'):
        self.min = min
        self.max = max
        self.width = max - min
        self.filled = filled
        self.unfilled = unfilled

    def update(self, val, message = ''):
        percent = val / self.width
        sys.stdout.write('\r[{0}{1}] {2}% :: {3}  '.format(self.filled * int(percent * 50), self.unfilled * (50 -  int(percent * 50)) , int(percent * 100), message))
        if val >= self.max:
            print("\n -- Finished --")
