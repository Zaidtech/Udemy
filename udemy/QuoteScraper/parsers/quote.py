from locators.quote_locator import QuoteLocator

"""
       Given one of the specific quote divs/element, find out the data about
       the quote content , author and tags
       parent is our provide dv
   """

class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'< Quote {self.content} by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocator.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocator.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tag(self):
        locator = QuoteLocator.TAGS
        return self.parent.select_one(locator) # will be a list

