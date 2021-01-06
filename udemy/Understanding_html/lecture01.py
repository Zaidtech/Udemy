from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
    <head>
        <title>This is title    </title>  
    </head>
    <body>
        <h1>This is title</h1>
        <p class="subtitle"> Lorem ipsum pisicing quod necessitatibus mollitia! Minus, minima ad.</p>
        <p>Another P without class </p>
        <ul>
            <li>ZAID</li>
            <li>Ali</li>
            <li>Wassaf</li>
            <li>Marium</li>
        </ul>
    </body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

h1_tag = simple_soup.find('h1')
print(h1_tag)


def find_list_item():
    list_item = simple_soup.find_all('li')
    list_contents = [data.string for data in list_item]
    print(list_contents)


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_all_para():
    paragraphs = simple_soup.find_all('p')
    print(paragraphs)
    #  get method by defalut return NONE if a key value error arises , however we can modify it
    # other_paragraphs = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', None)]
    #  instead of default like above  we can return empty list if not found in the class like below
    other_paragraphs = [p for p in paragraphs  if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraphs)
    print(other_paragraphs[0].string)


# find_list_item()
# find_subtitle()
find_all_para()
