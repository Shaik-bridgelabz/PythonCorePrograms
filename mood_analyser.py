class MoodAnalyser:

    def __init__(self, message):
        self.message = message

    def analysemood(self):
        from mood_analyser_exception import MoodAnalyserException
        try:
            if self.message is None:
                raise MoodAnalyserException(error=TypeError, message="Entered Null Value")
            if len(self.message) == 0:
                raise MoodAnalyserException(error=NameError, message="Entered empty Value")
            if "Sad" in self.message:
                return "SAD"
            else:
                return "HAPPY"
        finally:
            return "No error"
