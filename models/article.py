class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Invalid title")
        from .author import Author
        from .magazine import Magazine

        if not isinstance(author, Author):
            raise Exception("Invalid author")

        if not isinstance(magazine, Magazine):
            raise Exception("Invalid magazine")

        self._title = title   # immutable
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # title is immutable → ignore change
        pass