class Textual(str):
    class TextualFieldCannotBeEmpty(Exception):
        status_code = 400

    def __new__(cls, value):
        if not value:
            raise cls.TextualFieldCannotBeEmpty()

        return super.__new__(value)
