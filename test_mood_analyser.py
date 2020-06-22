from mood_analyser import MoodAnalyser
from mood_analyser_exception import MoodAnalyserException
from mood_analyser_factory import MoodAnalyserFactory


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


def test_analysemood_whengiventwoobjects_ifequals_shouldretunequal():
    moodAnalyserFactory = MoodAnalyserFactory(mood_analyser="Iam in Happy mood")
    mood1 = moodAnalyserFactory.mood_analyser
    mood2 = moodAnalyserFactory.mood_analyser
    assert mood1 == mood2

def test_analysemood_givenclassname_whenimproper_shouldthrowexception():
    moodAnalyserFactory = MoodAnalyserFactory(mood_analyser="Iam in Happy mood")
    try:
        mood1 = moodAnalyserFactory
        mood2 = moodAnalyserFactory.mood_analyser
    except MoodAnalyserException as e:
        assert e.type == MoodAnalyserException.NoSuchClassError
