import requests,bs4,lxml

base_url='https://books.toscrape.com/catalogue/page-{}.html'
'''
req=requests.get(base_url.format(2))

soup=bs4.BeautifulSoup(req.text,'lxml')
products=soup.select('.product_pod')

example=products[0]

print(example.select('a')[1]['title'])
'''
#########################################################

two_star_titles=[]

for n in range(1,51):
    scrap_url=base_url.format(str(n))
    print(scrap_url)
    req=requests.get(scrap_url)
    soup=bs4.BeautifulSoup(req.text,'lxml')
    books=soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two'))!=0:
            book_title=book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)


