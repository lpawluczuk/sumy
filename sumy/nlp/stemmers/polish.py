"""The code of the stem_word function relies on the polish stemmer found in this python module
pystempel (https://github.com/dzieciou/pystempel/).
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PolishStemmer(metaclass=Singleton):
    def __init__(self):
        try:
            from stempel import StempelStemmer
        except ImportError:
            # TODO
            raise ValueError("Polish stemmer requires pystempel. Please, install it by command 'pip install pystempel'.")

        self.stemmer = StempelStemmer.polimorf()

    def stem_word(self, word):
        """
        """
        return self.stemmer.stem(word.lower())

