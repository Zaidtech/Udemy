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

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    #  important can use t acess any element with attrs.[] method
    locater = 'article.product_pod h3 a '
    item_link = soup.select_one(locater)
    item_name = item_link.attrs['title']
    link = item_link.attrs['href']
    print(item_link)
    print(item_name)
    print(link)
    # print(link)


def find_item_price():
    locater_price = 'article.product_pod p.price_color '
    item_price = soup.select_one(locater_price)
    price_as_string = item_price.string
    expression = '[0-9 \.].+'
    price = (re.findall(expression, price_as_string.string))
    print(float(price[0]))


def find_rating():
    locater = 'article.product_pod p.star-rating'
    item_star = soup.select_one(locater)
    item_class = item_star.attrs['class']
    # print(item_class[1])    Can do this but it wount be the best thing to do
    item_rating = [r for r in item_class if r != 'star-rating']

    # item_rating = filter(lambda x: x!= 'star-rating', item_class) a more better way
    print(item_rating[0])


find_item_name()
find_item_price()
find_rating()
