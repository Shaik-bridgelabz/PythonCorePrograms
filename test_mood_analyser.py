from mood_analyser import MoodAnalyser


def test_analysemood():
    moodAnalyser = MoodAnalyser()
    mood = moodAnalyser.analysemood("Iam in Sad Mood")
    assert mood == "SAD"
