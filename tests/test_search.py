from president_speech.db.search import title, speech


def test_title():
    title(keyword="독립")


def test_speech():
    speech(keyword="독립")
