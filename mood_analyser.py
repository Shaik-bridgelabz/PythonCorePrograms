from mood_analyser_exception import MoodAnalyserException


class MoodAnalyser:

    def __init__(self, message):
        self.message = message

    def analysemood(self):
        if self.message is None:
            raise MoodAnalyserException(error=TypeError, message="Entered Null Value")
        if len(self.message) == 0:
            raise MoodAnalyserException(error=NameError, message="Entered empty Value")
        if "Sad" in self.message:
            return "SAD"
        else:
            return "HAPPY"

    def __eq__(self, that: object) -> bool:
        if super().__eq__(that):
            return super().__eq__(that)
        else:
            raise MoodAnalyserException(error=MoodAnalyserException, message="No such class found ")
