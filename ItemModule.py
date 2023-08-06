# Item class will be the data structure used to contain Books and Journals
# Items can be categorised using itemtype which can be either book aor journal

class Item:
    def __init__(self, itemid, itemtype, title, author, pyear, quantity, genre):
        self.itemid = itemid
        self.itemtype = itemtype
        self.title = title
        self.author = author
        self.pyear = pyear
        self.quantity = quantity
        self.genre = genre