class Logger:
    def __init__(self):
        self.log_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.log_dict and timestamp - self.log_dict[message] < 10:
            return False
        self.log_dict[message] = timestamp
        return True