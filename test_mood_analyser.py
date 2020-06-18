from mood_analyser import MoodAnalyser


def test_analysemood_whengivenmessage_sad_shouldreturn_sad():
    moodAnalyser = MoodAnalyser("Iam in Sad Mood")
    mood = moodAnalyser.analysemood()
    assert mood == "SAD"

def test_analysemood_whengivenmessage_happy_shouldreturn_happy():
    moodAnalyser = MoodAnalyser("Iam in Happy Mood")
    mood = moodAnalyser.analysemood()
    assert mood == "HAPPY"

def test_analysemood_whengivennullmessage_shouldreturn_happy():
    moodAnalyser = MoodAnalyser("null")
    mood = moodAnalyser.analysemood()
    assert mood == "HAPPY"
