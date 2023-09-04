from konlpy.tag import Kkma
kkma = Kkma()

def nonus(text: str) -> list:
    return kkma.nouns(text)
