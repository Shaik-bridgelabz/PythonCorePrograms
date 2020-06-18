class MoodAnalyser:

    def __init__(self, message):
        self.message = message

    def analysemood(self):
        try:
            if "Sad" in self.message:
                return "SAD"
            else:
                return "HAPPY"
        except NameError:
            return "HAPPY"



