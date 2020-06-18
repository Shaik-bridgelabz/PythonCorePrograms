class MoodAnalyser:

    def __init__(self, message):
        self.message = message

    def analysemood(self):
        if "Sad" in self.message:
            return "SAD"
        else:
            return "HAPPY"

