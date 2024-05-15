'''import requests
import bs4

web_text=requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')


soup=bs4.BeautifulSoup(web_text.text,'lxml')
computer=soup.select('.mw-file-description')[0]

image_link=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
with open('my_com_image.jpg','wb') as f:
    f.write(image_link.content)


'''
from . import web_scraping2