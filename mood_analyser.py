class MoodAnalyser:

    def __init__(self, message):
        self.message = message

    def analysemood(self):
        from mood_analyser_exception import MoodAnalyserException
        try:
            if "Sad" in self.message:
                return "SAD"
            else:
                return "HAPPY"
        except MoodAnalyserException as e:
            return e.type



