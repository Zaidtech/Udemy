import re
from bs4 import BeautifulSoup

ITEM_HTML = '''  <html><head></head><body>


<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
<article class="product_pod">
          <div class="image_container">
                        <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
          </div>

            <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>

            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">

        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
                </div>
                </article>
                </li>
</body>
</html>
'''


class ParsedItemLocater:
    """
    This is a class used to store the info about the locators instead of being inside tha ParsedItem class
      :)
    """
    NAME_LOCATOR = 'article.product_pod h3 a '
    RATING_LOCATOR = 'article.product_pod p.star-rating'
    LINK_LOCATOR = 'article.product_pod h3 a '
    PRICE_LOCATOR = 'article.product_pod p.price_color '


class ParsedItem:
    """ A class to take html page as input and find various properties """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        #  important can use to access any element with attrs.[] method
        locater = ParsedItemLocater.NAME_LOCATOR
        item_name = self.soup.select_one(locater)
        name = item_name.attrs['title']
        return name

    @property
    def price(self):
        locater = ParsedItemLocater.PRICE_LOCATOR
        item_price = self.soup.select_one(locater).string
        #  to extract the price of the item
        expression = '[0-9 \.].+'
        price = (re.findall(expression, item_price))
        return float(price[0])

    @property
    def link(self):
        locater = ParsedItemLocater.LINK_LOCATOR
        item_link = self.soup.select_one(locater)
        link = item_link.attrs['href']
        return  link

    @property
    def rating(self):
        locater = ParsedItemLocater.RATING_LOCATOR
        item_star = self.soup.select_one(locater)
        item_class = item_star.attrs['class']
        # print(item_class[1])    Can do this but it wount be the best thing to do
        item_rating = [r for r in item_class if r != 'star-rating']
        # item_rating = filter(lambda x: x!= 'star-rating', item_class) a more better way
        return item_rating[0]


item = ParsedItem(ITEM_HTML)
print("Name:-" +item.name)
print("Price:- {}".format(item.price))
print("Rating:-" +item.rating)
print("Link:-" +item.link)
