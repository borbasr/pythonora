import time


class Stopwatch:
    def __init__(self):
        self.start_at = None
        self.elapsed = 0.0

    def start(self):
        if self.start_at is None:
            self.start_at = time.perf_counter()

    def stop(self):
        if self.start_at is not None:
            self.elapsed += time.perf_counter() - self.start_at
            self.start_at = None

    def reset(self):
        self.start_at = None
        self.elapsed = 0.0

    def seconds(self):
        if self.start_at is None:
            return self.elapsed
        return self.start_at


sw = Stopwatch()
sw.start()
time.sleep(0.8)
sw.stop()
print(sw.seconds())
