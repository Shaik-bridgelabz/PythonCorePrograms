from mood_analyser import MoodAnalyser


def test_analysemood_whengivenmessage_sad_shouldreturn_sad():
    moodAnalyser = MoodAnalyser()
    mood = moodAnalyser.analysemood("Iam in Sad Mood")
    assert mood == "SAD"

def test_analysemood_whengivenmessage_happy_shouldreturn_happy():
    moodAnalyser = MoodAnalyser()
    mood = moodAnalyser.analysemood("Iam in Happy Mood")
    assert mood == "HAPPY"
