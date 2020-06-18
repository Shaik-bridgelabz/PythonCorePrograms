import null as null

from mood_analyser import MoodAnalyser


def test_analysemood_whengivenmessage_sad_shouldreturn_sad():
    moodAnalyser = MoodAnalyser("Iam in Sad Mood")
    mood = moodAnalyser.analysemood()
    assert mood == "SAD"


def test_analysemood_whengivenmessage_happy_shouldreturn_happy():
    moodAnalyser = MoodAnalyser("Iam in Happy Mood")
    mood = moodAnalyser.analysemood()
    assert mood == "HAPPY"


def test_analysemood_whengivennullmessage_shouldreturn_exception():
    from mood_analyser_exception import MoodAnalyserException
    try:
        moodAnalyser = MoodAnalyser("null")
        moodAnalyser.analysemood()
    except MoodAnalyserException as e:
        assert e.type == TypeError
