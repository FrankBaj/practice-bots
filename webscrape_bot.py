from bs4 import BeautifulSoup
import requests

html_doc = """
<html>
  <head>
    <title>The Title</title>
  </head>
  <body>
    <p><b>This is a paragraph.</b></p>
    <p class="story"> This is a story all about how, my life got flipped, turned upside down.
        <a href="http://test.com/elsie" class="sister">nothing</a>
        <a href="http://test.com/sarah" class="sister"></a>
    </p>
  </body>
</html>
"""

# soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify()) 
# print(soup.title.string)
# print(soup.p.b.string)
# print(soup.p['class'])
# print(soup.a['href'])

# print(soup.find(class_='story'))
# print(soup.findAll(['a','title']))

# print(soup.find(href="http://test.com/sarah"))

# p = soup.find(class_='story')
# print(p.contents)
# for child in p.children:
#     print(child)

# print(soup.a.parent)

# for p in soup.a.parents:
#     print(p.name)

# a = soup.a
# print(a.next_sibling.previous_sibling)

response = requests.get('https://en.wikipedia.org/wiki/Christian_Albert,_Duke_of_Holstein-Gottorp')
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify()) 

# print(soup.text)

## Get the text of the top level heading (H1)
print(soup.h1.text)

## Find how many second level heading tags there are
print(len(soup.findAll('h2')))

## Extract the href of the first link on the page
print(soup.a['href'])
