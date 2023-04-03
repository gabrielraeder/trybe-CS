class Log:
    def dispara_log(self, message):
        return message


class LogError:
    def __init__(self, log):
        self.log: Log = log
        self.color = "\033[91m"
        self.reset = "\033[0m"

    def dispara_log(self, message):
        return self.log.dispara_log(self.color + message + self.reset)


class LogWarning:
    def __init__(self, log):
        self.log: Log = log
        self.color = "\033[93m"
        self.reset = "\033[0m"

    def dispara_log(self, msg):
        return self.log.dispara_log(self.color + msg + self.reset)


class LogSuccess:
    def __init__(self, log):
        self.log: Log = log
        self.color = "\033[92m"
        self.reset = "\033[0m"

    def dispara_log(self, msg):
        return self.log.dispara_log(self.color + msg + self.reset)


if __name__ == "__main__":
    logger = Log()

    print(LogError(logger).dispara_log("Error"))
    print(LogWarning(logger).dispara_log("Warning"))
    print(LogSuccess(logger).dispara_log("Success"))
