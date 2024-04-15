import time

class Statistics:
    def __init__(self):
        self.total_requests = 0
        self.total_processing_ns = 0
        self.start_time = 0

    def start_processing(self) -> None:
        self.start_time = time.time_ns()
        self.total_requests += 1

    def end_processing(self) -> None:
        end_time = time.time_ns()
        self.total_processing_ns += ( end_time - self.start_time )

    def get_avg_processing_time_ns(self) -> int:
        return self.total_processing_ns // max(1, self.total_requests)
