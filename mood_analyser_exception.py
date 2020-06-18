class MoodAnalyserException(Exception):

    def __init__(self, error, message):
        self.error = error
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.error} -> {self.message}'
