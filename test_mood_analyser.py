from mood_analyser import MoodAnalyser
from mood_analyser_exception import MoodAnalyserException


def test_analysemood_whengivenmessage_sad_shouldreturn_sad():
    moodAnalyser = MoodAnalyser("Iam in Sad Mood")
    mood = moodAnalyser.analysemood()
    assert mood == "SAD"


def test_analysemood_whengivenmessage_happy_shouldreturn_happy():
    moodAnalyser = MoodAnalyser("Iam in Happy Mood")
    mood = moodAnalyser.analysemood()
    assert mood == "HAPPY"


def test_analysemood_whengivennullmessage_shouldreturn_exception():
    try:
        moodAnalyser = MoodAnalyser(None)
        moodAnalyser.analysemood()
    except MoodAnalyserException as e:
        assert e.type == TypeError


def test_analysemood_whengivenemptymessage_shouldreturn_exception():
    try:
        moodAnalyser = MoodAnalyser("")
        moodAnalyser.analysemood()
    except MoodAnalyserException as e:
        assert e.message == "Entered Empty Value"
